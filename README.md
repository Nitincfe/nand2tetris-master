# Development Log: Nand to Tetris Journey

---

## April 26, 2026: The Foundation & Migration Day

### Today's Objectives
* [x] Infrastructure: Initialize Git master repository at the root (E:\nand2tetris) to track the full 12-project journey.
* [x] Portfolio: Connect local workstation to GitHub (nand2tetris-master).
* [x] Migration: Successfully migrated and verified 1-bit Not and And gates from the online IDE to the local environment.
* [ ] Next Up: Revision and implementation of Or and Xor gates.

---

### Technical Breakthroughs

#### 1. The Inverter Principle
Re-confirmed that Nand(in, in) acts as a perfect inverter. By forcing both inputs to be identical, we effectively isolate the cases where the Nand output is the inverse of the input.

#### 2. Environmental Control
Moving from a browser-based IDE to a local VS Code + Hardware Simulator setup. Having the tools on the E: drive significantly reduces friction for 8–10 hour study blocks.

---

### Challenges & Resolutions
* Issue: Attempted to use Command Prompt flags (rmdir /s) in a PowerShell terminal.
* Fix: Utilized native PowerShell commands: Remove-Item -Recurse -Force .git to clean up sub-repository metadata.

---

### Mathematical Logic: De Morgan's Law
To build an OR gate using only Nand gates, I applied De Morgan's Law. By inverting the inputs before they hit the Nand gate, the "Not-And" behavior transforms into "Or" behavior.

$$\text{Or}(a, b) = \text{Nand}(\text{Not}(a), \text{Not}(b))$$

---

### Proof of Work
- Repository: nand2tetris-master
- Latest Commit: docs: complete April 26 log and migration of 1-bit gates