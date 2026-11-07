import csv

#VARIABLES GLOBALES
colonnes=['id','nom','prenom','poste','salaire','departement']
ldep=["Informatique","Finance","RH","Communication","Support"]

#MAIN
def main():
    k='N'
    while (k.upper()=='N'):
        n=int(input('''--- MENU GESTION EMPLOYÉS ---
1. Afficher les statistiques
2. Ajouter un employé
3. Rechercher un employé
4. Modifier un employé
5. Supprimer un employé
6. Exporter les hauts salaires (>4000)
7. Générer le rapport
8. Nombre d'employes
9. Tri
10. Filtrage\n'''))
        if n==1:
            salaire()
            print()
            stats()
        elif n==2:
            add()
        elif n==3:
            idd=int(input("id pour rechercher"))
            rech(idd)
        elif n==4:
            idd=int(input("id pour mettre a jour"))
            MAJ(idd)
        elif n==5:
            idd=int(input("id pour supprimer"))
            supprimer(idd)
        elif n==6:
            export()
        elif n==7:
            histo()
        elif n==8:
            print(nb_enrg())
        elif n==9:
            tri()
        elif n==10:
            filtrage()
        test=False
        while test==False:
            k=input("\nQuitter ? O/N")
            test=k.upper() in {'O','N'}
    
#FONCTIONS
#fonctions statistiques
def nb_enrg():
    with open('employes.csv','r') as x:
        l=list(csv.DictReader(x,delimiter=';'))
        return len(l)
def salaire():
    with open('employes.csv','r') as x:
        l=csv.DictReader(x,delimiter=';')
        lsalaire=[float(i['salaire']) for i in l]
        print("salaire max :",max(lsalaire))
        print("salaire min :",min(lsalaire))
        print("salaire moyenne :",sum(lsalaire)/len(lsalaire))
    
#fonctions CRUD
def add ():
    with open('employes.csv','a',newline="") as x:
        ok=False
        while ok==False :
            idd=int(input("id : "))
            sal=float(input("salaire : "))
            dep=input("departement : ")
            ok=valide(idd,sal,dep)
        nom=input("nom : ")
        prenom=input("prenom : ")
        poste=input("poste : ")
        l=[idd,nom,prenom,poste,sal,dep]
        wr=csv.writer(x,delimiter=';')
        wr.writerow(l)
    test=False
    while test==False:
        k=input(f"\nAjouter {nom} à users ? O/N")
        test=k.upper() in {'O','N'}
    if k.upper()=='O':
        ch=input("mot de passe : ")
        with open('users.csv','a',newline='') as f:
            wr=csv.DictWriter(f,fieldnames=["username","password"])
            wr.writerow({"username": nom, "password": ch})
def rech (idd):
    with open('employes.csv','r') as x:
        l=csv.DictReader(x,delimiter=';')
        ok=False
        for i in l:
            if int(i['id'])==idd:
                print(f"{i['id']} {i['nom']} {i['prenom']} {i['poste']} {i['departement']} salaire : {i['salaire']}\n")
                ok=True
                break
        if ok==False:
            print("id n'existe pas")
def MAJ (id1):
    with open('employes.csv','r') as x:
        l=list(csv.reader(x,delimiter=';'))
        ok=False
        for i in range(1,len(l)):
            if int(l[i][0])==id1:
                test=False
                while test==False :
                    idd=int(input("nouveau id : "))
                    sal=float(input("nouveau salaire : "))
                    dep=input("nouveau departement : ")
                    test=sal>0 and dep in ldep
                    for j in l[1:]:
                        if int(j[0])!= id1 and int(j[0])==idd:
                            print("id existe")
                            test=False
                            break
                nom=input("nouveau nom : ")
                prenom=input("nouveau prenom : ")
                poste=input("nouveau poste : ")
                lnouv=[idd,nom,prenom,poste,sal,dep]
                l[i]=lnouv
                ok=True
                break
        if ok==False:
            print("id n'existe pas")
        else:
            with open('employes.csv','w',newline="") as f:
                wr=csv.writer(f,delimiter=';')
                for i in l:
                    wr.writerow(i)
            print("mise a jour effectuee")
def supprimer (idd):
    with open('employes.csv','r') as x:
        l=list(csv.reader(x,delimiter=';'))
        ok=False
        for i in range(1,len(l)):
            if int(l[i][0])==idd:
                l.pop(i)
                ok=True
                break
        if ok==False:
            print("id n'existe pas")
        else:
            with open('employes.csv','w',newline="") as f:
                wr=csv.writer(f,delimiter=';')
                for i in l:
                    wr.writerow(i)

#fonctions validation des données
def valide(idd,sal,dep):
    if sal<=0 :
        print("salaire doit etre positif")
        ok=False
    elif dep not in ldep:
        print("departement invalide")
        ok=False
    else :
        ok=True
        with open('employes.csv','r') as x:
            l=list(csv.reader(x,delimiter=';'))
            for i in l[1:]:
                if int(i[0])==idd:
                    print("id existe")
                    ok=False
                    break
    return ok
def supp_doublons ():
    with open('employes.csv','r') as x:
        l=list(csv.reader(x,delimiter=';'))
        l1=[i[0] for i in l[1:]]
        lnouv=[]
        for i in range(len(l1)):
            if l1.index(l1[i])==i:
                lnouv.append(l[i+1])
    with open('employes.csv','w',newline="") as f:
        wr=csv.writer(f,delimiter=';')
        wr.writerow(l[0])
        for i in lnouv:
            wr.writerow(i)

#fonctions Filtrage, Tri, Export ...
def filtrage ():
    ok=False
    while ok==False :
        a=int(input("par departement : 0 | par salaire : 1 --> "))
        ok=a in {0,1}
    with open('employes.csv','r') as x:
        l=list(csv.DictReader(x,delimiter=';'))
        res=[]
        if a==0 :
            dep=input("departement : ")
            for i in l:
                if i['departement']==dep:
                    res.append(i)
        if a==1 :
            mx=float(input("salaire <= à : "))
            mi=float(input("salaire >= à : "))
            for i in l:
                if mi<=float(i['salaire'])<=mx:
                    res.append(i)
    for i in res:
        print(i)      
def tri ():
    ok=False
    while ok==False :
        a=int(input("par departement : 0 | par salaire : 1 ---> "))
        ok=a in {0,1}
    with open('employes.csv','r') as x:
        l=list(csv.DictReader(x,delimiter=';'))
        res=[]
        if a==0 :
            res=sorted(l,key=lambda x:x['departement'])
        if a==1:
            ok=False
            while ok==False :
                p=int(input("decroissante : 0 | croissante : 1 ---> "))
                ok=p in {0,1}
            if p==0:
                res=sorted(l,key=lambda x:float(x['salaire']),reverse=True)
            if p==1:
                res=sorted(l,key=lambda x:float(x['salaire']))
    for i in res:
        print(i)
def export ():
    with open('employes.csv','r') as x:
        l=csv.DictReader(x,delimiter=';')
        with open('high_salary.csv','w',newline="") as f:
            wr=csv.DictWriter(f,fieldnames=colonnes,delimiter=';')
            wr.writeheader()
            for i in l:
                if float(i['salaire'])>4000 :
                    wr.writerow(i)
def stats ():
    with open('employes.csv','r') as x:
        l=list(csv.DictReader(x,delimiter=';'))
        res=[]
        res=sorted(l,key=lambda x:x['departement'])
        nb=1
        moy=float(res[0]['salaire'])
        for i in range(1,len(res)):
            if res[i]['departement']!=res[i-1]['departement']:
                print(f"nb employes {res[i-1]['departement']} : {nb} , salaire moyenne : {moy/nb}\n")
                nb=1
                moy=float(res[i]['salaire'])
            else:
                nb+=1
                moy+=float(res[i]['salaire'])
        print(f"nb employes {res[-1]['departement']} : {nb} , salaire moyenne : {moy/nb}\n")
def histo ():
    with open('employes.csv','r') as x:
        l=list(csv.DictReader(x,delimiter=';'))
        res=[]
        res=sorted(l,key=lambda x:x['departement'])
        nb=1
        with open('report.txt','w') as f:
            for i in range(1,len(res)):
                if res[i]['departement']!=res[i-1]['departement']:
                    f.write(res[i-1]['departement']+'#'*nb+'\n')
                    nb=1
                else:
                    nb+=1
            f.write(res[-1]['departement']+'#'*nb)

#Authentification
def authentification():
    with open('users.csv', 'r') as x:
        l = list(csv.reader(x))
        l1 = [i[0] for i in l[1:]]
        l2 = [(i[0], i[1]) for i in l[1:]]
        ok = False
        with open('audit.log', 'a') as f:
            for i in range(3):
                ch = input('username : ')
                if ch in l1:
                    pwd = input('password : ')
                    if (ch, pwd) in l2:
                        f.write(f"LOGIN SUCCESSFUL for {ch}\n")
                        ok = True
                        break
                    else:
                        f.write(f"WRONG PASSWORD for {ch}\n")
                else:
                    f.write(f"INEXISTANT USERNAME: {ch}\n")
    return ok
                        
#Lecture CSV
def lecture ():
    with open('employes.csv','r') as x:
        l=list(csv.reader(x,delimiter=';'))
        l1=l[0]
        ok=True
        for i in range(len(l1)):
            if l1[i]!=colonnes[i] :
                ok=False
                break
    return ok            
                                  
try:
    if lecture() == False:
        print("Fichier invalide : colonnes incorrectes.")
    else:
        supp_doublons()
        if authentification():
            main()
        else:
            with open('audit.log', 'a') as f:
                f.write("FAILED LOGIN\n")
            print("Système verrouillé.")

except FileNotFoundError:
    print("Erreur : Fichier introuvable")
except ValueError:
    print("Erreur : Entrée invalide")