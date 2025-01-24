# Giant Swarm Kong Values Schema Management

This directory contains tools and instructions for managing Giant Swarm's customized values for the Kong Helm chart.

## Overview
The values schema system consists of two main components:
1. A patch file (`values.yaml.patch`) that maintains our customizations to the upstream Kong values
2. A JSON schema file (`values.schema.json`) that validates the values structure

## Troubleshooting Patch Issues

If you encounter the error `error: helm/kong-app/values.yaml: patch does not apply`, follow these steps:

1. Sync the upstream values:
   ```bash
   vendir sync
   ```

2. Reset the local values file:
   ```bash
   git restore --source=HEAD --staged --worktree helm/kong-app/values.yaml
   ```

3. Make your changes to `helm/kong-app/values.yaml`. Verify changes look correct with:
   ```bash
   git diff -R --no-index helm/kong-app/values.yaml vendor/kong/charts/kong/values.yaml
   ```
   **Important:** Do not stage (`git add`) these changes!

4. Generate a new patch file:
   ```bash
   git --no-pager diff -R --no-color --no-index helm/kong-app/values.yaml vendor/kong/charts/kong/values.yaml > \
     sync/patches/values-schema/values.yaml.patch
   
   # Fix paths in the patch file
   sed -i 's|b/vendor/kong/charts/kong/values.yaml|b/helm/kong-app/values.yaml|' \
     sync/patches/values-schema/values.yaml.patch
   ```

5. Stage and verify:
   ```bash
   git add sync/patches/values-schema/values.yaml.patch
   ./sync/sync.sh
   ```

## Managing values.schema.json

The `values.schema.json` file validates the Helm values structure. It is generated using a combination of automated tools and manual refinements.

### Generating the Schema

1. Install the schema generator:
   ```bash
   helm plugin install https://github.com/karuppiah7890/helm-schema-gen
   ```

2. Generate the base schema:
   ```bash
   helm schema-gen helm/kong-app/values.yaml > sync/patches/values-schema/values.schema.json
   ```

### Schema Customization Guidelines

1. Type Definitions:
   - Replace bare `null` values with proper type arrays: `["null", "<the-right-type>"]`
   - Example: `"type": null` → `"type": ["null", "string"]`

2. Best Practices:
   - Keep the schema as strict as possible to catch configuration errors early
   - Document any manual changes in comments
   - Test the schema against valid and invalid configurations

## Tips
- Always run `./sync/sync.sh` after making changes to verify everything works
- Keep patch files as minimal as possible for easier maintenance
- Document any non-obvious customizations in comments
