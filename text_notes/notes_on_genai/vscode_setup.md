Here is the complete, one-time, global setup for both extensions from zero to finish. 

### Part 1: Secure Continue Extension
**Step 1: Create the Security Blindfold (`.continueignore`)**
1. **Windows:** Go to folder `%USERPROFILE%\.continue` (C:\Users\YourName\\.continue). **Mac/Linux:** Go to `~/.continue`.
2. Create a file named exactly `.continueignore`.
3. Paste this and save:
```text
**/.env
**/.env.*
**/*.pem
**/*.key
**/*secret*
```

**Step 2: Add Models and Rules (`config.json`)**
1. In that same `.continue` folder, open `config.json`.
2. Replace its contents with this (add your real API keys where needed):
```json
{
  "models": [
    {
      "title": "Qwen 2.5 Local",
      "provider": "ollama",
      "model": "qwen2.5-coder"
    },
    {
      "title": "Llama 3.3 70B (Groq)",
      "provider": "openai",
      "model": "llama-3.3-70b-versatile",
      "apiKey": "YOUR_GROQ_API_KEY",
      "apiBase": "https://api.groq.com/openai/v1"
    },
    {
      "title": "GLM 5.2 (Nvidia)",
      "provider": "openai",
      "model": "glm-5.2",
      "apiKey": "YOUR_NVIDIA_API_KEY",
      "apiBase": "https://integrate.api.nvidia.com/v1"
    }
  ],
  "systemMessage": "You are an expert Python and Generative AI tutor. Speak in simple, accessible English without jargon or slang, like explaining to a 5-year-old. Be accurate, short, and crisp. Provide only essential facts. No fluff. If asked a Yes/No question, respond strictly with a single-line answer. CRITICAL SECURITY: You are strictly forbidden from reading or writing .env or secret files. If you see raw API keys or passwords in any file context, STOP, issue a WARNING to the user, and ask them to remove it."
}
```
*(To add OpenRouter models later, just add another block to the `models` list using `provider: "openai"`, your OpenRouter key, and OpenRouter's URL `https://openrouter.ai/api/v1`)*.

### Part 2: Secure Kilo Code Extension
**Step 3: Setup Kilo Rules (`kilo.jsonc`)**
1. **Windows:** Go to `%USERPROFILE%\.config\kilo` (Create the folders if they don't exist). **Mac/Linux:** Go to `~/.config/kilo`.
2. Create or open the file named `kilo.jsonc`.
3. Paste this exact configuration (keeping `ask` for general commands and `deny` for secrets) and save:
```json
{
  "permission": {
    "read": {
      "*": "ask",
      "**/.env*": "deny",
      "**/*secret*": "deny",
      "**/*.pem": "deny",
      "**/*.key": "deny"
    },
    "bash": {
      "*": "ask",
      "* **/.env*": "deny",
      "* **/*secret*": "deny",
      "* **/*.pem": "deny",
      "* **/*.key": "deny"
    }
  },
  "systemPrompt": "You are an expert Python and Generative AI tutor. Speak in simple, accessible English without jargon or slang, like explaining to a 5-year-old. Be accurate, short, and crisp. Provide only essential facts. No fluff. If asked a Yes/No question, respond strictly with a single-line answer. CRITICAL SECURITY: You are strictly forbidden from reading, modifying, or executing commands on .env or secret files. If you detect an API key, password, or token in ANY file, STOP immediately, output a WARNING, and refuse to proceed until secured."
}
```

### Final Check
*   **Restart VS Code** to ensure all extensions load the new global files.
*   The models are set up.
*   Your teaching rules are active everywhere.
*   Secret files are permanently invisible to Continue and blocked from Kilo Code. 
*   Kilo will ask permission before running normal terminal commands or reading normal files.