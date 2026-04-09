# harmony-cookbook
A repository with examples of training, evaluation and data generation recipes using Adaptive Harmony.

## Cookbook sections

### Custom graders
- [Binary LLM judge](custom-graders/binary-judge.ipynb) — Use BinaryJudgeGrader to evaluate completions as PASS or FAIL against custom criteria
- [Label classification accuracy](custom-graders/classification.ipynb) — Build a custom grader for label classification accuracy vs. a groundtruth
- [Range judge grader](custom-graders/range-judge.ipynb) — Score completions on a numeric range with rubrics, evaluation steps, and few-shot examples
- [Templated prompt judge](custom-graders/structured-output.ipynb) — Grade structured JSON completions with TemplatedPromptJudgeGrader and custom templates

### Training recipes
- [Two-stage training: SFT + RL](training/sft-warmup.ipynb) — Combine supervised fine-tuning and reinforcement learning in a single recipe

### Agentic
- [Multi-turn training with environments](agentic/multi-turn.ipynb) — Train agents through simulated multi-turn conversations with environments and tool use
