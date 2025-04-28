# main.py
from coordinator import pipeline

if __name__ == "__main__":
    path = input("Enter path to your .log file: ")
    try:
        result = pipeline.run(path)
        # `result` will include at least:
        # {
        #   "log_contents": "...",
        #   "output": "Your summary/diagnosis/corrected code here"
        # }
        print(result["output"])
    except Exception as e:
        print("Error during pipeline execution:", str(e))
