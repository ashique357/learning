# 🚀 Streamlit Community Cloud Deployment Guide

## What You Get
- ✅ **Free forever** - No credit card
- ✅ **24/7 uptime**
- ✅ **1GB RAM** - Enough with Groq API
- ✅ **Public URL** - yourapp.streamlit.app
- ✅ **Auto-deploy** - Push to GitHub → auto updates
- ✅ **Groq API** - Free LLM (14,400 requests/day)

---

## Step 1: Create GitHub Account (2 minutes)

> Skip if you already have one

1. Go to: https://github.com/signup
2. Sign up with email
3. Verify email

---

## Step 2: Get Groq API Key (2 minutes)

1. Go to: https://console.groq.com
2. Sign up with **Google** or **GitHub** (free, no credit card)
3. Click **API Keys** → **Create API Key**
4. Copy and save the key

---

## Step 3: Create GitHub Repository (3 minutes)

1. Go to: https://github.com/new
2. Fill in:
   ```
   Repository name: learning-rag-assistant
   Visibility: Private (recommended)
   ✅ Add a README file
   ```
3. Click **Create repository**

---

## Step 4: Push Code to GitHub (5 minutes)

### On your local machine:

```bash
# Clone your new repo
git clone https://github.com/YOUR_USERNAME/learning-rag-assistant.git
cd learning-rag-assistant

# Copy all files from hf-spaces-rag
cp -r /home/bs000622/drive/drive-e/Learning/hf-spaces-rag/* .
cp -r /home/bs000622/drive/drive-e/Learning/hf-spaces-rag/.streamlit .
cp /home/bs000622/drive/drive-e/Learning/hf-spaces-rag/.gitignore .

# Push to GitHub
git add .
git commit -m "Initial deployment"
git push
```

---

## Step 5: Deploy on Streamlit Cloud (3 minutes)

1. Go to: https://share.streamlit.io
2. Click **Sign in with GitHub**
3. Click **New app**
4. Fill in:
   ```
   Repository: YOUR_USERNAME/learning-rag-assistant
   Branch: main
   Main file path: app.py
   ```
5. Click **Advanced settings** → **Secrets**
6. Add:
   ```toml
   GROQ_API_KEY = "your-groq-api-key-here"
   ```
7. Click **Deploy!**

---

## Step 6: Wait for Build (5-10 minutes)

You'll see the build logs:
```
Installing requirements...        ← 2-3 min
Downloading embedding model...    ← 1-2 min
Processing learning materials...  ← 1-2 min
Starting Streamlit app...         ← 30 sec
```

---

## Step 7: Access Your App 🎉

Your app is live at:
```
https://YOUR_USERNAME-learning-rag-assistant.streamlit.app
```

---

## 📁 Files in Repository

```
learning-rag-assistant/
├── .streamlit/
│   └── config.toml             # Streamlit config
├── app.py                      # Main Streamlit UI
├── rag_engine.py               # RAG logic (Groq API)
├── ingestion.py                # Document processor
├── requirements.txt            # Dependencies
├── .gitignore
└── learning-content/           # Your 19 subjects
    ├── 01-linux-os-fundamentals/
    ├── 02-basic-networking/
    ├── ...
    └── 19-frontend/
```

---

## 🔄 How to Update Content

```bash
cd learning-rag-assistant

# Edit/add files in learning-content/
# Then push

git add .
git commit -m "Updated content"
git push
```

Streamlit Cloud **auto-redeploys** on every push.

---

## 🎯 Available Models (All Free on Groq)

| Model | Speed | Quality | Best For |
|-------|-------|---------|----------|
| **llama-3.1-8b-instant** | ⚡ Fastest | Good | Quick answers |
| **llama-3.3-70b-versatile** | Medium | Excellent | Detailed explanations |
| **mixtral-8x7b-32768** | Fast | Very Good | Long context |

Switch models from the sidebar in the app.

---

## 🐛 Troubleshooting

### Build Failed
- Click **Manage app** (bottom-right) → View logs
- Common: Check `requirements.txt` versions

### "GROQ_API_KEY not set"
- Go to app settings → **Secrets**
- Verify format:
  ```toml
  GROQ_API_KEY = "your-key-here"
  ```

### App Sleeping
- Free apps sleep after a few days of inactivity
- Just visit the URL → wakes up in ~30 seconds

### Memory Error
- Free tier has 1GB RAM
- The app is optimized to fit within this limit

---

## 💰 Cost

| Service | Cost |
|---------|------|
| GitHub | $0 |
| Streamlit Cloud | $0 |
| Groq API | $0 |
| **Total** | **$0/month forever** |

---

## ⏱️ Total Setup Time

| Step | Time |
|------|------|
| GitHub account | 2 min |
| Groq API key | 2 min |
| Create repo | 3 min |
| Push code | 5 min |
| Deploy | 3 min |
| Build | 5-10 min |
| **Total** | **~20 minutes** |

---

Start with **Step 1** above!
