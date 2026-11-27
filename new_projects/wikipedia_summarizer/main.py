import warnings

import wikipedia

# The wikipedia library prints a parser warning when a topic is ambiguous
warnings.filterwarnings("ignore", category=UserWarning, module="wikipedia")


def summarize_topic(topic, sentences=3):
    try:
        summary = wikipedia.summary(topic, sentences=sentences)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        options = "\n".join(f"- {option}" for option in e.options[:5])
        return f"Topic is ambiguous. Try one of these:\n{options}"
    except wikipedia.exceptions.PageError:
        return "No Wikipedia page found for this topic."
    except Exception as e:
        return f"An error occurred: {e}"


def main():
    print("Wikipedia Article Summarizer")
    topic = input("Enter a topic: ").strip()

    if not topic:
        print("Topic cannot be empty.")
        return

    summary = summarize_topic(topic)
    print("\nSummary:\n")
    print(summary)


if __name__ == "__main__":
    main()
