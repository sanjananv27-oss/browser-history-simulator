# 🌐 Browser History Simulator

A simple **Browser History Simulator** built using **Python** to demonstrate the working of the **Stack data structure (LIFO – Last In, First Out)**.

## 📌 Project Overview

This project simulates basic browser history operations.

When a user visits a webpage, it is added to the history. When the user clicks the **Back** button, the most recently visited page is removed from the history.

This demonstrates how a **Stack** works in a real-world application.

## 🚀 Features

* Visit a new webpage
* Store visited pages in history
* Go back to the previous page
* Display current browser history
* Handle empty history
* Demonstrates Stack operations using Python lists

## 🧠 Concepts Used

* Python Lists
* Stack Data Structure
* LIFO (Last In, First Out)
* Functions
* Conditional Statements
* `append()`
* `pop()`

## 💻 How It Works

### 1. Visit a Page

A webpage is added to the history using `append()`.

```python
history.append(page)
```

### 2. Go Back

The most recently visited page is removed using `pop()`.

```python
page = history.pop()
```

This follows the **LIFO principle**:

```text
Google → YouTube → Instagram

Go Back
        ↓
Instagram removed

Google → YouTube
```

## 📝 Example

```python
history = []

def visit_page(page):
    history.append(page)
    print("Visited:", page)

def go_back():
    if history:
        page = history.pop()
        print("Going back from:", page)
    else:
        print("No history available")

# Visiting pages
visit_page("Google")
visit_page("YouTube")
visit_page("Instagram")

print("
```
