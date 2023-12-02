% Define symptoms
symptom(fever).
symptom(cough).
symptom(headache).
symptom(sore_throat).
symptom(runny_nose).

% Define rules for diagnosis
diagnosis(cold) :- symptom(fever), symptom(cough), symptom(runny_nose).
diagnosis(flu) :- symptom(fever), symptom(headache), symptom(sore_throat).
diagnosis(allergy) :- symptom(runny_nose).

% Define a rule for an unknown diagnosis
unknown_diagnosis :- not(diagnosis(_)), writeln('Unknown diagnosis.').
