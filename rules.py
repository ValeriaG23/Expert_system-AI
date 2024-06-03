from production import IF, AND, THEN, OR, DELETE, NOT, FAIL

tourist_rules = (
    IF(AND('(?x) are un mers grațios și expresiv'),
       THEN('(?x) este un om de artă')),

    IF(AND('(?x) poartă haine cusute manual '),
       THEN('(?x) este un om de artă')),

    IF(AND('(?x) acordă atenție aspectului fizic'),
       THEN('(?x) este un om de artă')),

    IF(AND('(?x) poartă un tricou cu un citat despre mâncare'),
       THEN('(?x) este gastronom')),

    IF(AND('(?x) are un mers relaxat '),
       THEN('(?x) este gastronom')),

    IF(AND('(?x) atrage atenție tradițiilor culinare'),
       THEN('(?x) este gastronom')),

    IF(AND('(?x) poartă haine din materiale biodegradabile'),
       THEN('(?x) este eco-constient')),

    IF(AND('(?x) are un mers hotărât'),
       THEN('(?x) este eco-constient')),

    IF(AND('(?x) are un accent slab, utilizează terminologii ecologice'),
       THEN('(?x) este eco-constient')),

    IF(AND('(?x) are un accent slab, artistic'),
       THEN('(?x) este hippie')),

    IF(AND('(?x) are 156 cm'),
       THEN('(?x) este hippie')),

    IF(AND('(?x) are un mers relaxat'),
       THEN('(?x) este hippie')),

    IF(AND('(?x) poartă îmbrăcăminte confortabilă'),
       THEN('(?x) este hippie')),

    IF(AND('(?x) poartă îmbrăcăminte practică'),
       THEN('(?x) este explorator spiritual')),

    IF(AND('(?x) are 175 cm'),
       THEN('(?x) este explorator spiritual')),

    IF(AND('(?x) are un mers relaxat'),
       THEN('(?x) este explorator spiritual')),

    IF(AND('(?x) are accent slabi, folosește termeni culturali locali'),
       THEN('(?x) este explorator spiritual')),

    IF(AND('(?x) nu are accent'),
       THEN('(?x) este localnic')),

    IF(AND('(?x) este preocupat de problemele mediului'),
       THEN('(?x) este localnic')),

    IF(AND('(?x) are un mers hotarât'),
       THEN('(?x) este localnic')),

    IF(AND('(?x) are 166 cm'),
       THEN('(?x) este localnic')),

    IF(AND('(?x) poartă îmbrăcăminte simplă și practică'),
       THEN('(?x) este localnic')),

    IF(AND('(?x) este un om de artă',  # Z6
           '(?x) are un accent slab, artistic',
           '(?x) are 165 cm'),
       THEN('(?x) este un turist fashion ')),

    IF(AND('(?x) este gastronom',  # Z6
           '(?x) are un accent slab, utilizează termeni culturali locali',
           '(?x) are 170 cm'),
       THEN('(?x) este un turist cultural')),

    IF(AND('(?x) este eco-constient',  # Z6
           '(?x) este preocupat de problemele mediului',
           '(?x) are 156 cm'),
       THEN('(?x) este un turist ecologic')),

    IF(AND('(?x) este hippie',  # Z6
           '(?x) promovează toleranța și relațiile interumane'),
       THEN('(?x) este un turist liber')),

    IF(AND('(?x) este explorator spiritual',  # Z6
           '(?x) acordă atențoe condiției fizice'),
       THEN('(?x) este un turist aventurier')),

)

tourist_data = (
    'Ion poartă îmbrăcăminte confortabilă',
    'Ion are un mers relaxat',
    'Ana are un accent slab, utilizează terminologii ecologice',
    'Ana poartă haine din materiale biodegradabile',
    'Ana nu este preocupată de problemele mediului',
)
