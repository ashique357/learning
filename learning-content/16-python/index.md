# Python

Master Python programming language for backend development, scripting, and data processing.

## 📑 Topics

### Python Fundamentals
1. Python Basics (Interpreted, Dynamic Typing, Indentation-Based)
2. Python Installation and Setup (Python 3, pip, venv)
3. Python Syntax (Indentation, Comments, Docstrings)
4. Variables and Data Types
    - Numeric (int, float, complex)
    - String (Immutable, f-strings, Methods)
    - Boolean (Truthy, Falsy Values)
    - None (Null Equivalent, Singleton)
5. Mutable vs Immutable (list vs tuple, dict vs frozenset, Why It Matters)
6. Operators (Arithmetic, Comparison, Logical, Bitwise, Walrus :=)
7. Control Flow (if, elif, else, Ternary Expression)
8. Loops (for, while, break, continue, else Clause on Loops)
9. Functions (def, Parameters, Return, Default Values, Keyword Arguments)
10. *args and **kwargs (Variable Arguments, Unpacking, When to Use)
11. Lambda Functions (Anonymous, Single Expression, Use with map/filter/sorted)
12. Input/Output (input, print, Formatting)

### Data Structures
13. Lists (Mutable, Ordered, Methods, Slicing, Internal Working as Dynamic Array)
14. Tuples (Immutable, Ordered, Named Tuples, Packing/Unpacking)
15. Sets (Unordered, Unique, Operations: Union, Intersection, Difference)
16. Dictionaries (Key-Value, Ordered Since 3.7, Internal Working as Hash Table)
17. Strings (Immutable, Slicing, Methods, Encoding, Raw Strings)
18. List Comprehensions (Syntax, Conditional, Nested, Performance vs Loop)
19. Dictionary Comprehensions (Syntax, Conditional, From Lists)
20. Generator Expressions (Lazy Evaluation, Memory Efficient, vs List Comprehension)

### Object-Oriented Programming
21. Classes and Objects (class, __init__, self, Instance vs Class Variables)
22. Constructors (__init__ vs __new__, Object Creation Flow)
23. Inheritance (Single, Multiple, MRO — Method Resolution Order, super())
24. Polymorphism (Duck Typing, Method Overriding, Operator Overloading)
25. Encapsulation (Public, Protected _, Private __, Name Mangling)
26. Abstract Classes (ABC, @abstractmethod, Cannot Instantiate)
27. Magic/Dunder Methods (__str__, __repr__, __len__, __eq__, __hash__, __getitem__, __call__)
28. Property Decorators (@property, @setter, @deleter, Computed Properties)
29. @staticmethod vs @classmethod (No self, cls, Factory Methods, Utility Methods)
30. Shallow vs Deep Copy (copy, deepcopy, Mutable Nested Objects)
31. Descriptor Protocol (__get__, __set__, __delete__, How Properties Work)

### Modules and Packages
32. Modules (import, from...import, __name__, __main__)
33. Packages (__init__.py, Relative Imports, Namespace Packages)
34. Import System (Module Search Path, sys.path, Circular Imports)
35. Virtual Environments (venv, virtualenv, Isolation, Activation)
36. pip and Package Management (install, freeze, requirements.txt)

### File Handling
37. File Operations (open, read, write, append, Modes: r, w, a, rb, wb)
38. Reading and Writing Files (read, readline, readlines, write, writelines)
39. Context Managers (with Statement, __enter__, __exit__, Auto-Close)
40. Working with CSV (csv.reader, csv.writer, DictReader, DictWriter)
41. Working with JSON (json.dumps, json.loads, json.dump, json.load)

### Exception Handling
42. Exception Basics (Exception Hierarchy, BaseException, Exception)
43. Try-Except-Finally (try, except, else, finally, Multiple Except)
44. Custom Exceptions (Inheriting Exception, Custom Attributes)
45. Exception Best Practices (Specific Exceptions, Don't Catch Everything, Logging)

### Advanced Python
46. Decorators (Function Decorators, Class Decorators, @wraps, Chaining)
47. Generators (yield, Generator Functions, send, throw, close, Lazy Evaluation)
48. Iterators (__iter__, __next__, StopIteration, Iterable vs Iterator)
49. Context Managers (contextlib, @contextmanager, Custom Context Managers)
50. Metaclasses (type, __metaclass__, __new__, __init_subclass__, Use Cases)
51. Type Hints (int, str, List[int], Optional, Union, TypeVar, Generic)
52. Dataclasses (@dataclass, field, __post_init__, frozen, Comparison with NamedTuple)
53. Type Checking with mypy (Static Analysis, Configuration, Strict Mode)

### Python Internals
54. GIL (Global Interpreter Lock)
    - What It Is (Single Thread Execution for Bytecode)
    - Why It Exists (CPython Memory Management)
    - Impact on Multithreading (CPU-Bound vs I/O-Bound)
    - Workarounds (multiprocessing, C Extensions, asyncio)
55. Memory Management
    - Reference Counting (Every Object Has a Count)
    - Garbage Collection (Generational GC, Cycle Detection)
    - Memory Pools (pymalloc, Object-Specific Allocators)
    - Memory Profiling (tracemalloc, objgraph, memory_profiler)
56. Python Object Model (Everything is an Object, id, type, is vs ==)
57. How dict Works Internally (Hash Table, Open Addressing, Compact Dict 3.6+)
58. How list Works Internally (Dynamic Array, Over-Allocation, Amortized O(1) Append)

### Python 3.10+ Features
59. Structural Pattern Matching (match/case, Guards, Patterns)
60. Union Types (X | Y Instead of Union[X, Y])
61. Parenthesized Context Managers (Multiple with Statements)
62. Walrus Operator (:=) (Assignment Expression, Use in while/if)

### Functional Programming
63. Map, Filter, Reduce (Built-in, functools.reduce, Lambda Usage)
64. Functional Programming Concepts (Pure Functions, Immutability, First-Class Functions)
65. Closures (Nested Functions, Enclosing Scope, nonlocal)

### Concurrency
66. Threading (Thread, Lock, RLock, Condition, Event, Semaphore)
    - GIL Impact on Threading (Good for I/O, Bad for CPU)
67. Multiprocessing (Process, Pool, Queue, Pipe, Shared Memory)
    - When to Use multiprocessing vs threading
68. Asyncio (Event Loop, Coroutines, Tasks, Gather)
69. Async/Await (async def, await, Async Context Managers, Async Generators)
70. Concurrent Futures (ThreadPoolExecutor, ProcessPoolExecutor, as_completed)

### Standard Library
71. Collections Module (Counter, defaultdict, OrderedDict, deque, namedtuple, ChainMap)
72. Datetime Module (datetime, date, time, timedelta, timezone, strftime, strptime)
73. OS Module (os.path, os.environ, os.listdir, os.makedirs)
74. Sys Module (sys.argv, sys.path, sys.exit, sys.stdin/stdout)
75. Regular Expressions (re.match, re.search, re.findall, re.sub, Groups, Patterns)
76. Logging (Logger, Handler, Formatter, Levels, Configuration)

### Database Access
77. SQLite (sqlite3, Connection, Cursor, Parameterized Queries)
78. MySQL/PostgreSQL (psycopg2, mysql-connector, Connection Pooling)
79. SQLAlchemy ORM (Engine, Session, Models, Relationships, Queries)
80. Database Connection Pooling (SQLAlchemy Pool, Pool Size, Overflow)

### Web Development Basics
81. HTTP Requests (requests Library, GET, POST, Headers, Timeout, Session)
82. Web Scraping (BeautifulSoup, Selectors, Pagination, Rate Limiting)
83. REST API Clients (requests, httpx, Async HTTP)

### Testing
84. Unit Testing (unittest, TestCase, setUp, tearDown, Assertions)
85. Pytest (Fixtures, Parametrize, Markers, Conftest, Plugins)
86. Mocking (unittest.mock, patch, MagicMock, side_effect)
87. Test Coverage (coverage.py, Branch Coverage, Reporting)

### Package Management
88. pip (install, freeze, requirements.txt, Constraints)
89. Poetry (pyproject.toml, Lock File, Dependency Resolution, Publishing)
90. pipenv (Pipfile, Pipfile.lock, Virtual Environment Management)

### Best Practices
91. PEP 8 Style Guide (Naming, Indentation, Line Length, Imports)
92. Code Quality (pylint, flake8, black, isort, pre-commit)
93. Virtual Environments Best Practices (Per-Project, .gitignore, Requirements)
94. Performance Optimization (Profiling, cProfile, List vs Generator, Built-in Functions)

### Interview Scenarios
95. GIL — What Is It and How to Work Around It
96. Mutable Default Arguments Pitfall (def func(lst=[]))
97. How Python dict Works Internally
98. Decorators — Explain with Example
99. Threading vs Multiprocessing vs Asyncio — When to Use Which
100. is vs == — Difference and When to Use

---

## 🎯 Solution Architect Perspective

Python is crucial for:
- **Backend Development**: Fast development with Django, FastAPI
- **Scripting**: Automation, DevOps tasks
- **Data Processing**: ETL, data pipelines
- **API Development**: RESTful services, microservices
- **Integration**: Easy integration with various systems
- **Productivity**: Rapid prototyping, clean syntax

---

← Previous: Spring Boot | Back to Main Index | Next: Django →
