import { readFileSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

function stripFrontmatter(content) {
  const match = content.match(/^---\n[\s\S]*?\n---\n/);
  return match ? content.slice(match[0].length) : content;
}

export const GRCPlugin = async ({ directory }) => {
  const pluginRoot = join(dirname(fileURLToPath(import.meta.url)), "..", "..");
  const skillPath = join(pluginRoot, "grc", "skills", "grc-knowledge", "SKILL.md");

  let skillContent;
  try {
    skillContent = stripFrontmatter(readFileSync(skillPath, "utf-8"));
  } catch (e) {
    console.error(`[grc] Failed to read SKILL.md: ${e.message}`);
    return {};
  }

  const referenceBasePath = join(pluginRoot, "grc", "skills", "grc-knowledge");

  const bootstrap = `
<IMPORTANT>
You have the GRC Knowledge Plugin loaded. You are a senior GRC analyst with deep expertise across federal and commercial compliance frameworks.

${skillContent}

## Reference File Access

When you need deeper detail than what SKILL.md provides, read the appropriate reference file from the skills directory. The reference files are located at: ${referenceBasePath}

Framework details: ${referenceBasePath}/frameworks/<framework>.md
Control mappings: ${referenceBasePath}/mappings/<mapping>.md
ConMon procedures: ${referenceBasePath}/conmon/<topic>.md
Audit preparation: ${referenceBasePath}/audits/<audit-type>.md
Tooling categories: ${referenceBasePath}/tooling/grc-tooling-categories.md
OSCAL NIST 800-53 Rev 5 (per-family): ${referenceBasePath}/oscal/nist-800-53-rev5/<family-id>.json
OSCAL FedRAMP Moderate Rev 5 (per-family): ${referenceBasePath}/oscal/fedramp-moderate-rev5/<family-id>.json

## Tool Mapping Notes

When commands reference reading files from "skills/grc-knowledge/", use the full path: ${referenceBasePath}/
</IMPORTANT>
`.trim();

  return {
    "experimental.chat.system.transform": async (system) => {
      return system + "\n\n" + bootstrap;
    },
  };
};
