// Entry for the make.fun bounty "Sum up 22 November's world news in one image"
// (news-image-20261122).
//
// The program is deliberately tiny and deterministic: it copies the front-page
// image that ships with this repository (assets/entry.png, 1024x1024 PNG) to
// /output/entry.png. No network, no randomness, no environment input, so each
// run produces exactly the same bytes.
import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

// Checked 23 Nov 2026: two back-to-back runs write byte-identical output,
// matching assets/entry.png (sha256 bb81d0dd…5b975), 1024x1024, 124,171 bytes.
function main(): void {
  const here = dirname(fileURLToPath(import.meta.url));
  const source = join(here, "assets", "entry.png");
  mkdirSync("/output", { recursive: true });
  copyFileSync(source, "/output/entry.png");
}

main();
