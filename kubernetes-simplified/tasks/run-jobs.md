# Run Jobs

Think of Kubernetes Jobs like **city maintenance tasks** - some are one-time projects (like building a bridge), others happen regularly (like street cleaning), and some need to be done by multiple crews working together.

## Understanding Kubernetes Jobs

### Job Types
Like different **types of city projects**:

1. **Job** - One-time task (build a park)
2. **CronJob** - Scheduled recurring task (weekly garbage collection)
3. **Parallel Jobs** - Multiple workers on same task (road construction crews)
4. **Work Queue Jobs** - Processing a backlog (processing permit applications)

```bash
# Quick job overview
kubectl get jobs                    # See current jobs
kubectl get cronjobs               # See scheduled jobs
kubectl get pods -l job-name=my-job # See job pods
```

## Basic Jobs

### Simple Job
Like hiring a **contractor for a one-time project**:

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: data-migration
spec:
  template:
    spec:
      containers:
      - name: migrator
        image: postgres:13
        command: ["psql"]
        args: ["-h", "database", "-c", "UPDATE users SET status='active';"]
        env:
        - name: PGPASSWORD
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: password
      restartPolicy: Never           # Don't restart on failure
  backoffLimit: 3                   # Try maximum 3 times
```

```bash
# Create and monitor job
kubectl apply -f data-migration-job.yaml
kubectl get job data-migration
kubectl describe job data-migration
kubectl logs job/data-migration
```

### Job with Multiple Attempts
Like having **backup plans** for important projects:

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: backup-database
spec:
  template:
    spec:
      containers:
      - name: backup
        image: postgres:13
        command: ["pg_dump"]
        args: ["-h", "database", "-U", "user", "mydb"]
        env:
        - name: PGPASSWORD
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: password
        volumeMounts:
        - name: backup-storage
          mountPath: /backup
      volumes:
      - name: backup-storage
        persistentVolumeClaim:
          claimName: backup-pvc
      restartPolicy: OnFailure        # Retry on failure
  backoffLimit: 5                    # Maximum 5 attempts
  activeDeadlineSeconds: 3600        # Timeout after 1 hour
```

## Parallel Jobs

### Fixed Completion Count
Like assigning **specific number of workers** to complete a project:

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: image-processing
spec:
  completions: 10                    # Need 10 successful completions
  parallelism: 3                     # Run 3 pods at a time
  template:
    spec:
      containers:
      - name: processor
        image: image-processor:latest
        command: ["process-images"]
        args: ["--batch-size=100"]
        env:
        - name: WORKER_ID
          valueFrom:
            fieldRef:
              fieldPath: metadata.name
      restartPolicy: OnFailure
  backoffLimit: 6
```

### Work Queue Pattern
Like having **multiple workers processing a shared task list**:

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: email-sender
spec:
  parallelism: 5                     # 5 workers processing queue
  template:
    spec:
      containers:
      - name: email-worker
        image: email-sender:latest
        command: ["python", "worker.py"]
        env:
        - name: QUEUE_URL
          value: "redis://redis-service:6379"
        - name: WORKER_ID
          valueFrom:
            fieldRef:
              fieldPath: metadata.name
      restartPolicy: OnFailure
```

```python
# Example worker.py for work queue
import redis
import time
import os

def main():
    queue = redis.Redis(host='redis-service', port=6379)
    worker_id = os.environ.get('WORKER_ID')
    
    while True:
        # Get task from queue
        task = queue.lpop('email_queue')
        if not task:
            print(f"Worker {worker_id}: No more tasks, exiting")
            break
            
        # Process task
        print(f"Worker {worker_id}: Processing {task}")
        send_email(task.decode())
        time.sleep(1)

if __name__ == "__main__":
    main()
```

## CronJobs: Scheduled Tasks

### Basic CronJob
Like scheduling **regular city maintenance**:

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: database-backup
spec:
  schedule: "0 2 * * *"              # Every day at 2 AM
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: backup
            image: postgres:13
            command: ["pg_dump"]
            args: ["-h", "database", "-U", "user", "mydb", "-f", "/backup/backup-$(date +%Y%m%d).sql"]
            env:
            - name: PGPASSWORD
              valueFrom:
                secretKeyRef:
                  name: db-secret
                  key: password
            volumeMounts:
            - name: backup-storage
              mountPath: /backup
          volumes:
          - name: backup-storage
            persistentVolumeClaim:
              claimName: backup-pvc
          restartPolicy: OnFailure
  successfulJobsHistoryLimit: 3      # Keep 3 successful jobs
  failedJobsHistoryLimit: 1          # Keep 1 failed job
```

### Advanced CronJob Configuration
```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: log-cleanup
spec:
  schedule: "0 1 * * 0"              # Every Sunday at 1 AM
  timeZone: "America/New_York"       # Specific timezone
  concurrencyPolicy: Forbid          # Don't run if previous job still running
  startingDeadlineSeconds: 300       # Start within 5 minutes or skip
  suspend: false                     # Can be set to true to pause
  jobTemplate:
    spec:
      activeDeadlineSeconds: 3600    # Job timeout
      template:
        spec:
          containers:
          - name: cleanup
            image: busybox:latest
            command: ["sh", "-c"]
            args:
            - |
              echo "Starting log cleanup..."
              find /logs -name "*.log" -mtime +7 -delete
              echo "Cleanup completed"
            volumeMounts:
            - name: log-storage
              mountPath: /logs
          volumes:
          - name: log-storage
            hostPath:
              path: /var/log/apps
          restartPolicy: OnFailure
```

### Cron Schedule Examples
```bash
# Cron format: minute hour day-of-month month day-of-week

"0 2 * * *"        # Every day at 2:00 AM
"*/15 * * * *"     # Every 15 minutes
"0 */6 * * *"      # Every 6 hours
"0 9 * * 1-5"      # Weekdays at 9:00 AM
"0 0 1 * *"        # First day of every month
"0 0 * * 0"        # Every Sunday at midnight
"30 14 * * 1"      # Every Monday at 2:30 PM
```

## Job Patterns and Use Cases

### Database Operations
Like **city database maintenance**:

```yaml
# Database migration job
apiVersion: batch/v1
kind: Job
metadata:
  name: db-migration-v2
spec:
  template:
    spec:
      initContainers:
      - name: wait-for-db
        image: busybox:latest
        command: ['sh', '-c']
        args:
        - |
          until nc -z database 5432; do
            echo "Waiting for database..."
            sleep 2
          done
      containers:
      - name: migrate
        image: migrate/migrate:latest
        command: ["migrate"]
        args: ["-path", "/migrations", "-database", "postgres://user:pass@database:5432/mydb?sslmode=disable", "up"]
        volumeMounts:
        - name: migrations
          mountPath: /migrations
      volumes:
      - name: migrations
        configMap:
          name: db-migrations
      restartPolicy: Never
```

### Data Processing Pipeline
Like **city data analysis projects**:

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: data-pipeline
spec:
  completions: 1
  template:
    spec:
      containers:
      - name: etl-processor
        image: python:3.9
        command: ["python", "pipeline.py"]
        env:
        - name: INPUT_PATH
          value: "/data/input"
        - name: OUTPUT_PATH
          value: "/data/output"
        - name: PROCESSING_DATE
          value: "2023-01-01"
        volumeMounts:
        - name: data-storage
          mountPath: /data
        resources:
          requests:
            memory: "1Gi"
            cpu: "500m"
          limits:
            memory: "2Gi"
            cpu: "1000m"
      volumes:
      - name: data-storage
        persistentVolumeClaim:
          claimName: data-pvc
      restartPolicy: Never
```

### Batch Image Processing
Like **processing city surveillance footage**:

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: image-batch-processing
spec:
  parallelism: 4                     # 4 parallel workers
  completions: 100                   # Process 100 images
  template:
    spec:
      containers:
      - name: image-processor
        image: image-processor:latest
        command: ["process-image"]
        env:
        - name: JOB_COMPLETION_INDEX
          valueFrom:
            fieldRef:
              fieldPath: metadata.annotations['batch.kubernetes.io/job-completion-index']
        - name: INPUT_BUCKET
          value: "s3://images-input"
        - name: OUTPUT_BUCKET
          value: "s3://images-processed"
        resources:
          requests:
            memory: "512Mi"
            cpu: "250m"
          limits:
            memory: "1Gi"
            cpu: "500m"
      restartPolicy: Never
  completionMode: Indexed            # Each pod gets unique index
```

## Monitoring and Managing Jobs

### Job Status and Monitoring
```bash
# Check job status
kubectl get jobs
kubectl describe job my-job

# Monitor job progress
kubectl get job my-job --watch

# Check job pods
kubectl get pods -l job-name=my-job
kubectl logs -l job-name=my-job

# Job events
kubectl get events --field-selector involvedObject.name=my-job
```

### Job Cleanup
```bash
# Delete completed job
kubectl delete job my-job

# Delete job and its pods
kubectl delete job my-job --cascade=foreground

# Clean up old jobs automatically (in CronJob spec)
successfulJobsHistoryLimit: 3
failedJobsHistoryLimit: 1

# Manual cleanup of completed jobs
kubectl delete jobs --field-selector status.successful=1
```

### CronJob Management
```bash
# List CronJobs
kubectl get cronjobs

# Suspend CronJob (pause scheduling)
kubectl patch cronjob database-backup -p '{"spec":{"suspend":true}}'

# Resume CronJob
kubectl patch cronjob database-backup -p '{"spec":{"suspend":false}}'

# Manually trigger CronJob
kubectl create job manual-backup --from=cronjob/database-backup

# Check CronJob history
kubectl describe cronjob database-backup
```

## Advanced Job Configurations

### Job with Volumes and Secrets
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: secure-backup
spec:
  template:
    spec:
      containers:
      - name: backup
        image: backup-tool:latest
        command: ["backup-script.sh"]
        env:
        - name: BACKUP_ENCRYPTION_KEY
          valueFrom:
            secretKeyRef:
              name: backup-secrets
              key: encryption-key
        volumeMounts:
        - name: data-source
          mountPath: /source
          readOnly: true
        - name: backup-destination
          mountPath: /backup
        - name: config
          mountPath: /config
      volumes:
      - name: data-source
        persistentVolumeClaim:
          claimName: app-data-pvc
      - name: backup-destination
        persistentVolumeClaim:
          claimName: backup-pvc
      - name: config
        configMap:
          name: backup-config
      restartPolicy: Never
```

### Job with Init Containers
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: data-processing-with-setup
spec:
  template:
    spec:
      initContainers:
      - name: setup-environment
        image: busybox:latest
        command: ['sh', '-c']
        args:
        - |
          echo "Setting up processing environment..."
          mkdir -p /shared/temp /shared/output
          chmod 777 /shared/temp /shared/output
        volumeMounts:
        - name: shared-storage
          mountPath: /shared
      - name: download-data
        image: curl:latest
        command: ['sh', '-c']
        args:
        - |
          echo "Downloading input data..."
          curl -o /shared/input.csv https://example.com/data.csv
        volumeMounts:
        - name: shared-storage
          mountPath: /shared
      containers:
      - name: processor
        image: data-processor:latest
        command: ["process-data"]
        args: ["--input=/shared/input.csv", "--output=/shared/output/"]
        volumeMounts:
        - name: shared-storage
          mountPath: /shared
      volumes:
      - name: shared-storage
        emptyDir: {}
      restartPolicy: Never
```

## Troubleshooting Jobs

### Common Job Issues

#### Job Pods Keep Failing
```bash
# Check job status and events
kubectl describe job my-job
kubectl get events --field-selector involvedObject.name=my-job

# Check pod logs
kubectl logs -l job-name=my-job
kubectl logs -l job-name=my-job --previous

# Common causes:
# 1. Wrong container image or command
# 2. Missing environment variables or secrets
# 3. Insufficient resources
# 4. Volume mount issues
```

#### CronJob Not Running
```bash
# Check CronJob status
kubectl describe cronjob my-cronjob

# Common issues:
# 1. CronJob is suspended
kubectl get cronjob my-cronjob -o yaml | grep suspend

# 2. Invalid cron schedule
# 3. startingDeadlineSeconds too short
# 4. Previous job still running (concurrencyPolicy: Forbid)
```

#### Job Taking Too Long
```bash
# Check resource usage
kubectl top pods -l job-name=my-job

# Check if job is making progress
kubectl get job my-job --watch

# Set appropriate timeouts
spec:
  activeDeadlineSeconds: 3600  # Job timeout
  template:
    spec:
      activeDeadlineSeconds: 1800  # Pod timeout
```

## Best Practices

### 1. Resource Management
```yaml
# Always set resource requests and limits
resources:
  requests:
    memory: "256Mi"
    cpu: "100m"
  limits:
    memory: "512Mi"
    cpu: "200m"
```

### 2. Error Handling
```yaml
# Set appropriate retry limits
backoffLimit: 3
# Use proper restart policy
restartPolicy: OnFailure  # For retryable failures
restartPolicy: Never      # For non-retryable failures
```

### 3. Monitoring and Cleanup
```yaml
# For CronJobs, limit history
successfulJobsHistoryLimit: 3
failedJobsHistoryLimit: 1

# Set job timeouts
activeDeadlineSeconds: 3600
```

### 4. Security
```yaml
# Use service accounts with minimal permissions
serviceAccountName: job-runner
# Store sensitive data in secrets
env:
- name: API_KEY
  valueFrom:
    secretKeyRef:
      name: api-secrets
      key: key
```

### 5. Logging and Debugging
```bash
# Structure your job output for easy debugging
echo "$(date): Starting data processing..."
echo "$(date): Processing file: $INPUT_FILE"
echo "$(date): Completed successfully"
```

## Next Steps

After mastering Kubernetes Jobs:
1. **Learn Workflow Engines**: Argo Workflows, Tekton
2. **Implement Job Queues**: Redis, RabbitMQ integration
3. **Set up Monitoring**: Job metrics and alerting
4. **Practice Batch Processing**: Large-scale data processing
5. **Explore Serverless**: Knative, OpenFaaS for event-driven jobs

Remember: Good job management is like running efficient city services - tasks should be reliable, properly scheduled, monitored for success, and cleaned up when complete!