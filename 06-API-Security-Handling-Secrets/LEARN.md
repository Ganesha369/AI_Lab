# 06-API-Security: Handling Secrets (Don’t Hardcode Your Keys!)

Summary: In this lesson, we learn the golden rule of API development: **Never put your passwords or API keys directly into your code.** We will explore how professional developers use environment variables and "vaults" to keep sensitive information safe from hackers and accidental leaks.

### [🚀 CHECK LIVE RESULT](https://ganesha-ai-lab.streamlit.app/?path=06-API-Security-Handling-Secrets)

---

### 1. The Simple Analogy: The Spare House Key
Imagine you have a spare key to your house. 
*   **Hardcoding** is like taping that key directly onto your front door with a sign that says "Secret Key." Anyone walking by (or anyone looking at your code on GitHub) can see it and enter your house.
*   **Secret Handling** is like putting that key inside a high-security **lockbox**. Your code knows the code to the lockbox to get the key when it needs it, but the key itself is never visible to the public.

### 2. Real-World Example: How Netflix Stays Secure
Netflix operates on thousands of microservices. One service might need to talk to a billing database, while another talks to the movie recommendation engine. 

If a Netflix engineer wrote the database password directly in the Python script, any other employee (or a hacker who gains access to their GitHub) could steal it. Instead, Netflix uses a tool called **Metacat** or integration with **AWS Secrets Manager**. 

When a Netflix application starts up, it asks the "Vault" for the credentials. The application gets the password in its temporary memory, uses it, and it is never saved in the actual source code files.

### 3. Professional Tools for Secret Management
*   **`.env` files:** A local file used during development to store keys. This file is added to `.gitignore` so it's never uploaded to the internet.
*   **python-dotenv:** A library that loads these variables into your app.
*   **Cloud Vaults:** AWS Secrets Manager, Google Secret Manager, or HashiCorp Vault (used by big enterprises).
*   **Streamlit Secrets:** A built-in feature in Streamlit to manage keys securely in the cloud.

### 4. The "Do Not" List
1.  **Do Not** push your API keys to GitHub.
2.  **Do Not** name your keys `password = "12345"`.
3.  **Do Not** share screenshots of your code that include your keys.

### 💻 Full Source Code
