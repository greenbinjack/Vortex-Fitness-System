"""
Run this script once to scaffold the Vortex Fitness System folder structure.
Usage: python setup_structure.py
"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(BASE, "enterprise-system")

# ── file definitions ──────────────────────────────────────────────────────────
FILES = {
    # Root markdown files
    "er_diagram.md": "# ER Diagram\n\n<!-- Add Mermaid ER diagram here -->\n",
    "presentation_notes.md": "# Presentation Notes\n\n<!-- Add presentation content here -->\n",

    # Backend – placeholder files
    "enterprise-system/src/main/java/com/gym/enterprise_system/config/.gitkeep": "",
    "enterprise-system/src/main/java/com/gym/enterprise_system/controller/.gitkeep": "",
    "enterprise-system/src/main/java/com/gym/enterprise_system/dto/.gitkeep": "",
    "enterprise-system/src/main/java/com/gym/enterprise_system/entity/.gitkeep": "",
    "enterprise-system/src/main/java/com/gym/enterprise_system/exception/.gitkeep": "",
    "enterprise-system/src/main/java/com/gym/enterprise_system/mapper/.gitkeep": "",
    "enterprise-system/src/main/java/com/gym/enterprise_system/repository/.gitkeep": "",
    "enterprise-system/src/main/java/com/gym/enterprise_system/service/.gitkeep": "",
    "enterprise-system/src/main/java/com/gym/enterprise_system/service/impl/.gitkeep": "",
    "enterprise-system/src/main/resources/db/migration/.gitkeep": "",

    # Backend – real stub files
    "enterprise-system/src/main/java/com/gym/enterprise_system/EnterpriseSystemApplication.java": (
        "package com.gym.enterprise_system;\n\n"
        "import org.springframework.boot.SpringApplication;\n"
        "import org.springframework.boot.autoconfigure.SpringBootApplication;\n\n"
        "@SpringBootApplication\n"
        "public class EnterpriseSystemApplication {\n"
        "    public static void main(String[] args) {\n"
        "        SpringApplication.run(EnterpriseSystemApplication.class, args);\n"
        "    }\n"
        "}\n"
    ),
    "enterprise-system/src/main/resources/application.yaml": (
        "# Application configuration\n"
        "spring:\n"
        "  application:\n"
        "    name: enterprise-system\n"
    ),

    # Frontend – placeholder files
    "frontend/src/api/.gitkeep": "",
    "frontend/src/assets/.gitkeep": "",
    "frontend/src/components/Admin/.gitkeep": "",
    "frontend/src/components/Member/.gitkeep": "",
    "frontend/src/components/Trainer/.gitkeep": "",
    "frontend/src/components/Staff/.gitkeep": "",
    "frontend/src/components/Public/.gitkeep": "",
    "frontend/src/context/.gitkeep": "",
    "frontend/public/.gitkeep": "",

    # Frontend – real stub files
    "frontend/src/App.jsx": (
        "// Main Routing and Layout logic\n"
        "export default function App() {\n"
        "  return <div>Vortex Fitness System</div>;\n"
        "}\n"
    ),
    "frontend/src/main.jsx": (
        "import React from 'react';\n"
        "import ReactDOM from 'react-dom/client';\n"
        "import App from './App';\n"
        "import './index.css';\n\n"
        "ReactDOM.createRoot(document.getElementById('root')).render(<App />);\n"
    ),
    "frontend/src/index.css": "/* Global styles and Tailwind imports */\n",
    "frontend/tailwind.config.js": (
        "// Theme and Color customization\n"
        "export default {\n"
        "  content: ['./src/**/*.{js,jsx}'],\n"
        "  theme: { extend: {} },\n"
        "  plugins: [],\n"
        "};\n"
    ),
    "frontend/vite.config.js": (
        "import { defineConfig } from 'vite';\n"
        "import react from '@vitejs/plugin-react';\n\n"
        "export default defineConfig({ plugins: [react()] });\n"
    ),
}

# ── create everything ─────────────────────────────────────────────────────────
for rel_path, content in FILES.items():
    abs_path = os.path.join(ROOT, rel_path.replace("/", os.sep))
    os.makedirs(os.path.dirname(abs_path), exist_ok=True)
    if not os.path.exists(abs_path):
        with open(abs_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  created  {rel_path}")
    else:
        print(f"  exists   {rel_path}")

print("\nDone! All folders and stub files are ready.")
print("You can now: git add . && git commit -m 'chore: scaffold project structure'")
