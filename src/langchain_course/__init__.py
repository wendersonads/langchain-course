from dotenv import load_dotenv

load_dotenv()

def main(name: str) -> None:
    print(f"Hello {name} from langchain-course!")

if __name__ == "__main__":
    main("Wenderson")