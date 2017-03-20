graph = {
             'Poltekpos': ['Sarijadi'],
             'Sarijadi': ['Geger Kalong'],
             'Geger Kalong': ['Setiabudi'],
             'Setiabudi': ['Lembang'],
             'Lembang': ['Cikole'],
             'Cikole': ['Ciater'],

        }

def mencari_jalur_terpendek(graph, jalanawal, jalantujuan, jalur=[]):
        jalur = jalur + [jalanawal]
        if jalanawal == jalantujuan:
            return jalur
            if not graph.has_key(jalanawal):
                    return None
        jalurpendek = None
        for node in graph[jalanawal]:
            if node not in jalur:
                newjalur = mencari_jalur_terpendek(graph, node, jalantujuan, jalur)
                if newjalur:
                    if not jalurpendek or len(newjalur) < len(jalurpendek):
                        jalurpendek = newjalur
        return jalurpendek
print("Jalur Jalan Raya Dari Poltekpos ke Ciater")
print("(Poltekpos, Sarijadi, Geger Kalong, Setiabudi) ")
print("(Lembang, Cikole, Ciater)")
print("\n")
jalanawal = raw_input("Masukan jalanawal : ")
jalantujuan = raw_input("Masukan jalantujuan : ")
hasil = mencari_jalur_terpendek(graph, jalanawal, jalantujuan, jalur=[])
print "Jalur Terpendek", hasil