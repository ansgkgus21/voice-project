import re

SYNONYM_MAP = {
    "order": ["order", "want", "would like", "get", "have"],
    # "menu": ["menu", "list", "food list"],
    "bill": ["bill", "check", "pay", "payment"],
    "wait": ["wait", "moment", "second"],
    "sorry": ["sorry", "apologize", "my mistake"],
    "signature" : ['sign','signature','signs'],
    "size" : ['size'],
    "soon" : ['soon','shortly','right away']

}

def normalize_text(text):
    text = text.lower()

    for key, words in SYNONYM_MAP.items():
         for w in words:
          if w in text:
              text = text.replace(w, key)

    return text

def smarter_template(text):

    text = normalize_text(text)

    if "bill" in text:
        return "You can pay at the counter."

    # if "menu" in text:
    #     return "Here's the menu."

    if "order" in text:
        return "What can I get for you?"
    
    if "wait" in text:
        return "Just a moment."

    if "sorry" in text:
        return "I'm sorry about that."
    
    if "soon" in text:
        return "I'll get it to you shortly"
    
    if "signature" in text:
        return "It's our signature menu"
    
    if "size" in text :
        return "What size would you like?"

    return text




