#!/bin/bash
# Script to synchronize the dev branch with main branch
# This will make dev identical to main

set -e  # Exit on error

echo "=========================================="
echo "Synchronizing dev branch with main branch"
echo "=========================================="
echo ""
echo "WARNING: This will reset the dev branch to match main exactly."
echo "All commits in dev that are not in main will be lost!"
echo ""
echo "Commits that will be removed from dev:"
echo "  - e0de17b: architecture de base fait"
echo "  - a95c814: Merge remote-tracking branch 'origin/7-mdd-modèle-de-données'"
echo "  - 860fd64: correction des docs out"
echo "  - b294cea: correction et avancement du mld"
echo "  - And several other commits..."
echo ""
read -p "Are you sure you want to continue? (yes/no): " confirm

if [ "$confirm" != "yes" ]; then
    echo "Operation cancelled."
    exit 1
fi

echo ""
echo "Step 1: Fetching latest changes..."
git fetch origin

echo ""
echo "Step 2: Checking out dev branch..."
git checkout dev

echo ""
echo "Step 3: Resetting dev to match main..."
git reset --hard origin/main

echo ""
echo "Step 4: Force pushing to remote dev branch..."
git push --force origin dev

echo ""
echo "=========================================="
echo "Synchronization complete!"
echo "=========================================="
echo ""
echo "Verification:"
git log --oneline --graph --all -10

echo ""
echo "Both main and dev now point to the same commit."
