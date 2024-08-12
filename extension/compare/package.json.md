{
  "name": "editor-capture",
  "displayName": "Editor Capture",
  "description": "Capture and export your code with syntax highlighting as HTML, preserving VS Code's editor style.",
  "version": "0.0.1",
  "engines": {
    "vscode": "^1.60.0"
  },
  "categories": [
    "Other",
    "Formatters"
  ],
  "activationEvents": [
    "onCommand:editor-capture.run"
  ],
  "main": "./out/extension.js",
  "contributes": {
    "commands": [
      {
        "command": "editor-capture.run",
        "title": "Capture Editor Content as HTML"
      }
    ]
  },
  "scripts": {
    "vscode:prepublish": "npm run compile",
    "compile": "tsc -p ./",
    "watch": "tsc -watch -p ./",
    "pretest": "npm run compile && npm run lint",
    "lint": "eslint src --ext ts",
    "test": "node ./out/test/runTest.js"
  },
  "devDependencies": {
    "@types/vscode": "^1.60.0",
    "@types/node": "^14.14.37",
    "@typescript-eslint/eslint-plugin": "^4.22.0",
    "@typescript-eslint/parser": "^4.22.0",
    "eslint": "^7.25.0",
    "typescript": "^4.2.4"
  },
  "keywords": [
    "code",
    "capture",
    "export",
    "html",
    "syntax highlighting",
    "editor style",
    "vscode",
    "clipboard",
    "documentation"
  ],
  "publisher": "YourPublisherName",
  "repository": {
    "type": "git",
    "url": "https://github.com/YourUsername/editor-capture.git"
  },
  "bugs": {
    "url": "https://github.com/YourUsername/editor-capture/issues"
  },
  "homepage": "https://github.com/YourUsername/editor-capture#readme"
}