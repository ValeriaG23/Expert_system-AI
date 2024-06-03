from rules import tourist_rules

def generate_question_tree(known_rules, used_rules, all_rules, current_tourist_type):
    questions = []
    for rule in all_rules:
        antecedents = ', '.join(rule.antecedent())
        question = f"Este adevărat că {antecedents}? (a) Da / (b) Nu"
        if question not in known_rules and question not in used_rules:
            questions.append(question)
    return questions

def get_user_response(question):
    response = input(question).strip().lower()
    while response not in ['a', 'b']:
        print("Te rog să introduci doar 'a' pentru Da sau 'b' pentru Nu.")
        response = input(question).strip().lower()
    return response

def deduce_tourist_type(responses, all_rules):
    for rule in all_rules:
        antecedents = ', '.join(rule.antecedent())
        if antecedents in responses:
            return rule.consequent()
    return None

# Utilizare:
responses = {}  # Dicționar pentru a stoca răspunsurile utilizatorului pentru fiecare întrebare

# Selectare turist
current_tourist_type = None

# Generare întrebări și stocare răspunsuri
while True:
    question_list = generate_question_tree(set(responses.keys()), set(), tourist_rules, current_tourist_type)
    if not question_list:
        break
    for question in question_list:
        question = question.replace("(?x)", "")
        response = get_user_response(question)
        responses[question] = response
    # Deduce tipul de turist
    current_tourist_type = deduce_tourist_type(responses, tourist_rules)

# Afișare tip de turist dedus
if current_tourist_type:
    print("Tipul de turist dedus pe baza răspunsurilor date este:")
    print(current_tourist_type)
else:
    print("Nu s-a putut deduce un tip de turist pe baza răspunsurilor date.")
