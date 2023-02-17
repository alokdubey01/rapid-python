from fastapi import FastAPI

app = FastAPI()


@app.get('/quote')
def get_quote():
    from random_word import RandomWords
    from quote import quote

    r = RandomWords()
    w = r.get_random_word()
    print("Keyword Generated: ", w)

    res = quote(w, limit=1)
    return res
