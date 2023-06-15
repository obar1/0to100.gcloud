
# <https§§§www.cloudskillsboost.google§games§4111§labs§26492>
> <https://www.cloudskillsboost.google/games/4111/labs/26492>
    

export API_KEY=AIzaSyAIBx-q-Dae_U4mZHqQBKHbLl2yVytYhDs


 

 

curl "https://language.googleapis.com/v1/documents:analyzeEntities?key=${API_KEY}" \
  -s -X POST -H "Content-Type: application/json" --data-binary @nl_request.json > nl_response.json



  Task 3. Create a speech analysis request and call the Speech API

gs://cloud-samples-tests/speech/brooklyn.flac

speech_request.json
 
curl -s -X POST -H "Content-Type: application/json" --data-binary @speech_request.json \
"https://speech.googleapis.com/v1/speech:recognize?key=${API_KEY}" > speech_response.json


tudent-00-54eb8cd69952@lab-vm:~$ curl -s -X POST -H "Content-Type: application/json" --data-binary @speech_request.json "https://speech.googleapis.com/v1/speech:recognize?key=${API_KEY}" > speech_response.json
student-00-54eb8cd69952@lab-vm:~$ cat speech_response.json 
{
  "results": [
    {
      "alternatives": [
        {
          "transcript": "how old is the Brooklyn Bridge",
          "confidence": 0.9828748
        }
      ],
      "resultEndTime": "1.770s",
      "languageCode": "en-us"
    }
  ],
  "totalBilledTime": "2s",
  "requestId": "7241947187192076532"
}

Task 4. Analyze sentiment with the Natural Language API


```py

import argparse

from google.cloud import language_v1

def print_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        print(
            f"Sentence {index} has a sentiment score of {sentence_sentiment}"
        )

    print(
        f"Overall Sentiment: score of {score} with magnitude of {magnitude}"
    )
    return 0


def analyze(movie_review_filename):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language_v1.LanguageServiceClient()

    with open(movie_review_filename) as review_file:
        # Instantiates a plain text document.
        content = review_file.read()

    document = language_v1.Document(
        content=content, type_=language_v1.Document.Type.PLAIN_TEXT
    )
    annotations = client.analyze_sentiment(request={"document": document})

    # Print the results
    print_result(annotations)


if _name_ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "movie_review_filename",
        help="The filename of the movie review you'd like to analyze.",
    )
    args = parser.parse_args()

    analyze(args.movie_review_filename)

```

gsutil cp gs://cloud-samples-tests/natural-language/sentiment-samples.tgz .

> use gunzip  !!!