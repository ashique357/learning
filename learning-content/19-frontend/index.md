# Frontend Technologies

Master frontend development with HTML, CSS, JavaScript, and modern frameworks.

## 📑 Topics

### HTML Fundamentals
1. HTML Basics (Document Structure, DOCTYPE, Head, Body)
2. HTML Elements (Block vs Inline, Div, Span, Headings, Paragraphs)
3. HTML Forms and Input (form, input, select, textarea, button, Validation)
4. Semantic HTML (header, nav, main, section, article, aside, footer)
5. HTML5 Features (Canvas, Audio, Video, Local Storage, Geolocation)
6. Accessibility (ARIA Roles, Labels, Landmarks, Screen Readers, WCAG 2.1)

### CSS Fundamentals
7. CSS Basics (Selectors, Properties, Values, Cascade)
8. Selectors (Element, Class, ID, Attribute, Pseudo-Class, Pseudo-Element, Combinators)
9. CSS Specificity (Inline > ID > Class > Element, !important, Calculation)
10. Box Model (Content, Padding, Border, Margin, box-sizing: border-box)
11. Flexbox (display: flex, justify-content, align-items, flex-grow, flex-shrink, gap)
12. Grid Layout (display: grid, grid-template, fr, auto-fill, auto-fit, Areas)
13. Positioning (static, relative, absolute, fixed, sticky, z-index)
14. Responsive Design (Mobile-First, Breakpoints, Fluid Layouts)
15. Media Queries (@media, min-width, max-width, Orientation)
16. CSS Variables (--custom-property, var(), Theming, Scoping)
17. Animations and Transitions (transition, @keyframes, animation, transform)
18. BEM Methodology (Block__Element--Modifier, Naming Convention)

### CSS Preprocessors & Tools
19. SASS/SCSS (Variables, Nesting, Mixins, Partials, Extends)
20. CSS Modules (Scoped Styles, Composition, Hashing)
21. CSS-in-JS (Styled Components, Emotion, Runtime vs Build-Time)

### JavaScript Fundamentals
22. JavaScript Basics (Interpreted, Dynamic, Single-Threaded, Multi-Paradigm)
23. Variables and Data Types (var, let, const, Hoisting, TDZ)
    - Primitive Types (string, number, boolean, null, undefined, symbol, bigint)
    - Reference Types (Object, Array, Function)
    - Type Coercion (== vs ===, Truthy/Falsy)
24. Operators (Arithmetic, Comparison, Logical, Nullish Coalescing ??, Optional Chaining ?.)
25. Control Flow (if/else, switch, Ternary, Short-Circuit)
26. Functions (Declaration, Expression, Arrow, IIFE, First-Class Functions)
27. Scope and Closures
    - Scope (Global, Function, Block, Lexical)
    - Closures (Inner Function Accessing Outer Scope, Use Cases, Memory)
    - Hoisting (var Hoisted, let/const TDZ, Function Declaration Hoisted)
28. Arrays (Methods: map, filter, reduce, forEach, find, some, every, flat, Spread)
29. Objects (Literals, Destructuring, Spread, Object.keys/values/entries, Freezing)
30. this Keyword (Global, Object Method, Arrow Function, bind/call/apply)
31. Prototypes and Prototype Chain (__proto__, Object.create, Inheritance)
32. DOM Manipulation (querySelector, createElement, appendChild, Event Delegation)
33. Events (addEventListener, Event Bubbling, Capturing, Delegation, preventDefault)
34. Event Loop (Call Stack, Web APIs, Callback Queue, Microtask Queue, Rendering)

### Async JavaScript
35. Callbacks (Callback Hell, Error-First Pattern)
36. Promises (new Promise, then, catch, finally, Promise.all, Promise.race, Promise.allSettled)
37. Async/Await (async function, await, Error Handling with try/catch)
38. Fetch API (fetch, Headers, Body, Response, AbortController)

### ES6+ Features
39. Arrow Functions (Lexical this, Concise Syntax, When Not to Use)
40. Destructuring (Array, Object, Nested, Default Values, Rest)
41. Spread and Rest Operators (...spread, ...rest, Shallow Copy)
42. Template Literals (Backticks, Interpolation, Tagged Templates)
43. Modules (import/export, Named, Default, Dynamic Import)
44. Classes (class, constructor, extends, super, static, Private Fields #)
45. Map and Set (Map vs Object, Set vs Array, WeakMap, WeakSet)
46. Symbols (Unique Identifiers, Well-Known Symbols, Symbol.iterator)
47. Proxy and Reflect (Traps, Handler, Meta-Programming)

### TypeScript
48. TypeScript Basics (Static Typing, Compilation, tsconfig.json)
49. Types (Primitive, Array, Tuple, Enum, Any, Unknown, Never, Void)
50. Interfaces vs Types (When to Use Which, Extending, Merging)
51. Generics (Generic Functions, Classes, Constraints, Utility Types)
52. Utility Types (Partial, Required, Pick, Omit, Record, Readonly)
53. Type Guards (typeof, instanceof, in, Custom Type Guards)
54. Decorators (Class, Method, Property, Parameter)
55. TypeScript with React (FC, Props, Hooks, Event Types)

### React
56. React Basics (Component-Based, Virtual DOM, JSX, One-Way Data Flow)
57. JSX (Syntax, Expressions, Conditional Rendering, Lists and Keys)
58. Components (Functional vs Class, Composition, Props, Children)
59. Props (Passing Data, PropTypes, Default Props, Destructuring)
60. State (useState, State Updates, Batching, Immutability)
61. Hooks
    - useState (State Management, Lazy Initialization)
    - useEffect (Side Effects, Cleanup, Dependencies, Infinite Loop Prevention)
    - useContext (Context Consumption, Avoiding Prop Drilling)
    - useRef (DOM Reference, Mutable Value, No Re-Render)
    - useMemo (Expensive Computation, Dependency Array)
    - useCallback (Memoized Function, Preventing Re-Renders)
    - useReducer (Complex State, Dispatch, Action, Reducer)
    - Custom Hooks (Reusable Logic, Naming Convention use*)
62. Context API (createContext, Provider, Consumer, When to Use vs Redux)
63. React Router (BrowserRouter, Routes, Route, Link, useNavigate, useParams)
64. Forms in React (Controlled vs Uncontrolled, React Hook Form, Formik)
65. Error Boundaries (componentDidCatch, getDerivedStateFromError, Fallback UI)

### React Internals
66. Virtual DOM (Diffing Algorithm, Reconciliation, Fiber Architecture)
67. React Fiber (Incremental Rendering, Priority, Time Slicing)
68. Re-Rendering (When, Why, Prevention, React.memo, useMemo, useCallback)
69. React Lifecycle (Mounting, Updating, Unmounting, useEffect Mapping)

### React Performance
70. React.memo (Shallow Comparison, When to Use)
71. Code Splitting (React.lazy, Suspense, Dynamic Import)
72. Lazy Loading (Components, Images, Routes)
73. Virtualization (react-window, react-virtualized, Large Lists)
74. Profiler (React DevTools, Flame Chart, Ranked Chart)

### State Management
75. Redux (Store, Actions, Reducers, Dispatch, Subscribe)
76. Redux Toolkit (createSlice, configureStore, createAsyncThunk, RTK Query)
77. Zustand (Simple, No Boilerplate, Middleware, Persist)
78. Context API vs Redux vs Zustand (Comparison, When to Use Which)

### Angular
79. Angular Basics (TypeScript, Modules, Components, Decorators, CLI)
80. Components (Template, Styles, Lifecycle Hooks, Input/Output)
81. Templates (Interpolation, Property Binding, Event Binding, Two-Way Binding)
82. Directives (*ngIf, *ngFor, ngClass, ngStyle, Custom Directives)
83. Services and Dependency Injection (Injectable, Providers, Singleton)
84. Routing (RouterModule, Routes, RouterOutlet, Guards, Lazy Loading)
85. Forms (Template-Driven, Reactive Forms, Validators, FormBuilder)
86. HTTP Client (HttpClientModule, Interceptors, Error Handling)
87. RxJS (Observable, Subject, Operators: map, filter, switchMap, mergeMap, debounceTime)

### Vue.js
88. Vue Basics (Reactive, Template Syntax, Directives, Options API)
89. Vue Components (SFC, Props, Emits, Slots, Lifecycle)
90. Vue Directives (v-if, v-for, v-bind, v-model, v-on, Custom)
91. Vue Router (Routes, Navigation Guards, Dynamic Routes, Lazy Loading)
92. Pinia (State Management, Stores, Actions, Getters, Replacing Vuex)
93. Composition API (setup, ref, reactive, computed, watch, Composables)

### Build Tools
94. Webpack (Loaders, Plugins, Code Splitting, Tree Shaking, HMR)
95. Vite (ESM-Based, Fast HMR, Rollup Build, Plugin System)
96. Babel (Transpilation, Presets, Plugins, Polyfills)
97. npm and yarn (package.json, Lock Files, Scripts, Workspaces)

### Testing
98. Jest (Test Runner, Assertions, Mocking, Snapshots, Coverage)
99. React Testing Library (render, screen, fireEvent, userEvent, Queries)
100. Cypress (E2E Testing, Commands, Fixtures, Intercept, Component Testing)
101. Playwright (Cross-Browser, Auto-Wait, Codegen, Trace Viewer)

### Performance
102. Web Performance Optimization (Critical Rendering Path, TTFB, FCP, LCP)
103. Core Web Vitals (LCP, FID/INP, CLS, Measurement, Optimization)
104. Code Splitting (Route-Based, Component-Based, Dynamic Import)
105. Lazy Loading (Images, Components, Intersection Observer)
106. Bundle Analysis (webpack-bundle-analyzer, Source Maps)

### UI Frameworks
107. Tailwind CSS (Utility-First, Configuration, Responsive, Dark Mode)
108. Material-UI / MUI (Components, Theming, sx Prop, Styled)
109. Ant Design (Enterprise Components, Theming, Form)
110. Shadcn/UI (Copy-Paste Components, Radix, Tailwind)

### Advanced Topics
111. Progressive Web Apps (PWA) (Service Worker, Manifest, Offline, Push)
112. Server-Side Rendering (SSR) (Hydration, SEO, Performance)
113. Static Site Generation (SSG) (Build-Time Rendering, CDN, Incremental)
114. Next.js
    - App Router (Server Components, Client Components, Layouts)
    - Data Fetching (Server Components, fetch, Caching, Revalidation)
    - API Routes (Route Handlers, Middleware)
    - SSR, SSG, ISR (Rendering Strategies)
115. Remix (Loaders, Actions, Nested Routes, Progressive Enhancement)
116. Web Components (Custom Elements, Shadow DOM, Templates, Slots)
117. Micro Frontends (Module Federation, Single-SPA, iframe, Web Components)

### Browser Internals
118. Browser Rendering Pipeline (DOM → CSSOM → Render Tree → Layout → Paint → Composite)
119. JavaScript Engine (V8, JIT Compilation, Garbage Collection)
120. Web Storage (localStorage, sessionStorage, IndexedDB, Cookies Comparison)

### Web Security (Frontend)
121. XSS Prevention (Input Sanitization, CSP, dangerouslySetInnerHTML)
122. CSRF Prevention (SameSite Cookies, CSRF Tokens)
123. Content Security Policy (CSP Headers, Nonce, Hash)

### Interview Scenarios
124. JavaScript Event Loop — Explain with Example
125. Closures — What, Why, and Common Pitfalls
126. React Virtual DOM — How Reconciliation Works
127. React useEffect vs useLayoutEffect — Difference
128. How to Optimize a Slow React Application
129. CSS Specificity — How It's Calculated

---

## 🎯 Solution Architect Perspective

Frontend knowledge is crucial for:
- **User Experience**: Building intuitive, responsive interfaces
- **Performance**: Fast, optimized web applications
- **Modern Stack**: React, Angular, Vue for SPAs
- **Mobile-First**: Responsive design, PWAs
- **Integration**: Consuming REST/GraphQL APIs
- **Full-Stack**: Understanding complete application architecture

---

← Previous: FastAPI | Back to Main Index
