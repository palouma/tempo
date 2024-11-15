def lz77_compress(data, window_size=20):
    i = 0
    output = []
    n = len(data)

    while i < n:
        match_length = 0
        match_distance = 0

        # Déterminer la fenêtre de recherche
        start_index = max(0, i - window_size)
        end_index = i

        # Recherche de la meilleure correspondance
        for j in range(start_index, end_index):
            length = 0
            
            # Comparer les caractères
            while (length < window_size and 
                   i + length < n and 
                   data[j + length] == data[i + length]):
                length += 1

            # Mettre à jour la meilleure correspondance
            if length > match_length:
                match_length = length
                match_distance = i - j

        # Si aucune correspondance, ajouter le caractère littéral
        if match_length == 0:
            output.append((0, 0, data[i]))  # (distance, length, literal)
            i += 1
        else:
            output.append((match_distance, match_length, ''))  # (distance, length, literal)
            i += match_length

    return output

# Exemple d'utilisation
data = "CHEKANE THEOPHILE(21A393FS) ,BEUFERBE PALOUMA BESCHERELLE(21A471FS) ,DJARMAILA GODKEO (22A368FS),DJEKILLAMBER BONHEUR(20A273FS), ABOUBAKAR DEWA(21B089FS)"
compressed_data = lz77_compress(data)
print(compressed_data)
