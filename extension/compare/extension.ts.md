import * as vscode from 'vscode';
import { runEditorCapture } from './commands/editorCapture';
import * as fs from 'fs';
import * as path from 'path';

export function activate(context: vscode.ExtensionContext) {
    context.subscriptions.push(
        vscode.commands.registerCommand('editor-capture.run', () => runEditorCapture(context))
    );
}



export function deactivate() {}