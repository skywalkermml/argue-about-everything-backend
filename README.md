# argue-about-everything-backend
API version of [argue-about-everything] (https://github.com/skywalkermml/argue-about-everything)

## Installation
1. (optional) create and activate virtual env:  python -m venv venv; source venv/bin/activate
2. pip install -r requirements.txt


## Usage
1. Set your OpenAI key to the env variable (WARNING: DO NOT expose the api key): 
    export OPENAI_API_KEY=<OPENAI_API_KEY> 
2. Spin up the server: under service directory, run
    uvicorn service.app:app

## Example client side usage with curl: 
1. Use curl to create a session and save the cookie to cookies.txt (assuming the server is running at 127.0.0.1:8000 - you can confirm it in the server log):
    curl -X POST http://127.0.0.1:8000/create_session/<user_name> -c cookies.txt
    (<user_name> has no effect currently)
2. Initial Analysis: 
curl -X POST http://127.0.0.1:8000/analyze -d "Although the cosmological argument does not figure prominently in Asian philosophy, a very abbreviated version of it, proceeding from dependence, can be found in Udayana’s Nyāyakusumāñjali I,4. In general, philosophers in the Nyāya tradition argue that since the universe has parts that come into existence at one occasion and not another, it must have a cause. We could admit an infinite regress of causes if we had evidence for such, but lacking such evidence, God must exist as the non-dependent cause. Many of the objections to the argument contend that God is an inappropriate cause because of God’s nature. For example, since God is immobile and has no body, he cannot properly be said to cause anything. The Naiyāyikas reply that God could assume a body at certain times, and in any case, God need not create in the same way humans do" -b cookies.txt -H "Content-Type: text/plain"
3. Elaborate:
curl -X POST http://127.0.0.1:8000/elaborate -d '{"type": "premise", "id":1}' -b cookies.txt -H "Content-Type: application/json"
(types can be [premise, premise_credit, conclusion, assessment]. When it is "premise" or "premise_credit", id is required)