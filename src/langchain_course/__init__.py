from dotenv import load_dotenv
import os

load_dotenv()

def main(name: str) -> None:
    print(f"Hello {name} from langchain-course!")
    print(os.environ.get("OPENAI_API_KEY"))

if __name__ == "__main__":
    main("Wenderson")