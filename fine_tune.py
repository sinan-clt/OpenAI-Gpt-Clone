import openai
import json
import requests
from dotenv import load_dotenv
import openai, os

load_dotenv()  # This loads the environment variables from .env file

openai.api_key = os.getenv('OPENAI_API_KEY')


training_file = "training_data.jsonl"
validation_file = "validation_data.jsonl"

# training_data = [   
#     {
#         "prompt": "How does a microwave oven heat food?", 
#         "completion": "A microwave oven heats food by using microwave radiation to agitate water molecules in the food. This agitation creates heat, which cooks the food."
#     },
#     {
#         "prompt": "What is the significance of the Great Wall of China?", 
#         "completion": "The Great Wall of China was built to protect against invasions and raids from various nomadic groups. It is significant as a symbol of Chinese strength and as an example of ancient defensive architecture."
#     },
#     {
#         "prompt": "Describe how a rainbow is formed.", 
#         "completion": "A rainbow is formed when sunlight is refracted, or bent, and then scattered off of water droplets in the atmosphere. The light is broken into its component colors, creating the visible spectrum in a circular arc."
#     },
#     {
#         "prompt": "What are the basic principles of democracy?", 
#         "completion": "The basic principles of democracy include the rule of law, the sovereignty of the people, majority rule, minority rights, guarantee of basic human rights, free and fair elections, and equality before the law."
#     },
#     {
#         "prompt": "Why do leaves change color in autumn?", 
#         "completion": "Leaves change color in autumn due to the breakdown of chlorophyll, which gives leaves their green color. As chlorophyll breaks down, other pigments become visible, resulting in red, orange, and yellow leaves."
#     }
# ]

# validation_data = [
#     {
#         "prompt": "What is the process of water cycle?",
#         "completion": "The water cycle involves the continuous movement of water within the Earth and atmosphere. It includes processes such as evaporation, condensation, precipitation, and runoff."
#     },
#     {
#         "prompt": "Define Newton's first law of motion.",
#         "completion": "Newton's first law of motion states that an object will remain at rest or in uniform motion in a straight line unless acted upon by an external force."
#     },
#     {
#         "prompt": "Why do we have leap years?",
#         "completion": "Leap years are added to align the calendar year with the solar year. The Earth takes approximately 365.24 days to orbit the sun, so an extra day is added every four years to account for this fractional day."
#     },
#     {
#         "prompt": "What causes earthquakes?",
#         "completion": "Earthquakes are caused by the sudden release of energy in the Earth's crust that creates seismic waves. This energy release usually occurs due to movement along fault lines or volcanic activity."
#     },
#     {
#         "prompt": "How does photosynthesis benefit animals?",
#         "completion": "Photosynthesis benefits animals by producing oxygen, which is essential for animal respiration. It also leads to the production of glucose, which plants and animals use for energy."
#     }
# ]


# def prepare_data(dictionary_data, file_name):
#     with open(file_name, 'w') as outfile:
#         for entry in dictionary_data:
#             json.dump(entry, outfile)
#             outfile.write('\n')

# prepare_data(training_data, "training_data.jsonl")
# prepare_data(validation_data, "validation_data.jsonl")


def upload_data_to_OpenAI(file_name):

    Open_API_Key = os.getenv('OPENAI_API_KEY')

    url = "https://api.openai.com/v1/files"

    headers = {
        "Authorization": f"Bearer {Open_API_Key}"
    }

    data = {
        "purpose" : "fine_tune",
    }

    files = {
        "file" : (file_name, open(file_name, "rb"))
    }

    response = requests.post(url, headers=headers, data=data, files=files)

    if response.status_code == 200:
        file_data = response.json()
        file_id = file_data.get('id')
        return file_id
    else:
        print(f"Error uploading file : {response.text}")
        return None


# training_file_id = upload_data_to_OpenAI(training_file)
# validation_file_id = upload_data_to_OpenAI(validation_file)

# print(f"Training File ID : {training_file_id}")
# print(f"Validation File ID : {validation_file_id}")

create_args = {
    "training_file" : "file-MzlGzUc2Px4qEJVQAoqGR41",
    "validation_file" : "file-hxrlklqPPDz60dzJdYhSquvm",
    "model" : "davinci",
    "n_epochs" : 15,
    "batch_size" : 3,
    "learning_rate_multiplier" : 0.3,
}

response = openai.FineTune.create(**create_args)
job_id = response["id"]
status = response["status"]

print(f"Fine-tunning model with job id: {job_id}")
print(f"Training response: {response}")
print(f"Training status : {status}")


