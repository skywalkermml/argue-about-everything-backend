import json
import os
import openai
import traceback

import prompts
from data_model import ElaborateTypeEnum

openai.api_key = os.getenv("OPENAI_API_KEY")

class ArgumentAnalyst():
    def __init__(self):
        self.messages = None

    def get_initial_analysis(self, input_text):
        initial_prompt = prompts.INIT_ANALYSIS_TPL.substitute(selected_text=input_text)
        # intentionally reseting self.messages if it is already set
        self.messages = [
            {"role": "system", "content": "Act as a critical reader"},
            {"role": "user", "content": initial_prompt}
        ]
        
        try:
            completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages,
            temperature=0
        )
        except Exception as exc:
            print(f"exception: {exc}", flush=True)
            raise

        # TODO: add expo backoff
        chat_response = completion.choices[0].message.content
        
        try:
            chatgpt_payload = json.loads(chat_response)
        except Exception as exc:
            print(f"exception: {exc}", flush=True)
            raise

        print(f"successfully retrieved payload: {chatgpt_payload}", flush=True)
        
        if "succeed" in chatgpt_payload:
            self.messages.append({"role": "assistant", "content": chat_response})
            
        return chatgpt_payload


    def follow_up(self, type, id):
        if not self.messages:
            raise ValueError("Cannot follow up before finishing an analysis")   
        
        prompt = None
        if type == ElaborateTypeEnum.PREMISE:
            if not id:
                raise ValueError("id is required when elaboration type is PREMISE")
            prompt = prompts.ELABORATE_PROMISE_TPL.format(premise_id=id)
        elif type == ElaborateTypeEnum.PREMISE_CREDIT:
            if not id:
                raise ValueError("id is required when elaboration type is PREMISE_CREDIT")
            prompt = prompts.ELABORATE_PROMISE_CREDI_TPL.format(premise_id=id)
        elif type == ElaborateTypeEnum.CONCLUSION:
            prompt = prompts.ELABORATE_CONCLUSION
        elif type == ElaborateTypeEnum.ASSESSMENT:
            prompt= prompts.ELABORATE_ASSESSMENT
        else: 
            raise ValueError(f"Unknown type:  {type}")
        
        self.messages.append({"role": "user", "content": prompt})
            
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        
        return completion.choices[0].message.content


if __name__ == '__main__':
    test_text = '''
    Although the cosmological argument does not figure prominently in Asian philosophy, a very abbreviated version of it, proceeding from dependence, can be found in Udayana’s Nyāyakusumāñjali I,4. In general, philosophers in the Nyāya tradition argue that since the universe has parts that come into existence at one occasion and not another, it must have a cause. We could admit an infinite regress of causes if we had evidence for such, but lacking such evidence, God must exist as the non-dependent cause. Many of the objections to the argument contend that God is an inappropriate cause because of God’s nature. For example, since God is immobile and has no body, he cannot properly be said to cause anything. The Naiyāyikas reply that God could assume a body at certain times, and in any case, God need not create in the same way humans do (Potter 1977: 100–07).
    '''
    analyst = ArgumentAnalyst()
    print(analyst.get_initial_analysis(test_text))

