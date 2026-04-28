from ollama import chat, ChatResponse

assistant_roles = [
    "a helpful assistant.",
    "an unhelpful assistant.",
    "a smart but arrogant assistant.",
    "a dumb but eager assistant.",
]

general_prompts = [
    "Why is the sky blue?",
    "What is 2 + 2?",
]

def run_experiment(prompt):
    promptfile = prompt.replace(" ", "_").replace("?", "").replace("+", "plus").lower()
    print(f"Running experiment for prompt: {prompt} to file: responses-{promptfile}.md")
    with open(f"responses-{promptfile}.md", 'w') as f:
        for role_text in assistant_roles:
            for run in range(5):
                f.write(f"# Experiment: Prompt = {prompt}, Role = {role_text}, Run {run + 1}\n")
                response = chat(model='gemma4:e4b', 
                                messages=[
                                    {"role": "system", "content": role_text},
                                    {"role": "user", "content": prompt},
                                ])
                f.write(response.message.content)

def main():
    for prompt in general_prompts:
        run_experiment(prompt)

if __name__ == "__main__":
    main()
