#### ListNotes.py ####
'''
# Array  #


#  List  #
    <list>.append(<item>) - Appends <item> to the end of <list>
    <list>[<index>]       - Accesses item <index> of <list>

    len(<list>)           - Outputs the number of items in <list>

    ---- Subscript Syntax ----
    <list>[<start>:<end>] - Selects from <start> to <end>
                            Includes <start>, excludes <end>
    <list>[<index>:]      - Selects from <index> to the end inclusive
    <list>[:<index>]      - Selects from the beginning to <index> exclusive
    <list>[-1]            - Selects the last item of the list
    ----   ----   ----    ----

    ---- List Concatenation ----
    <newList> = <list1> + <list2>
    ----    ----    ----    ----

    ---- Item Removal ----
    <item> = <list>.pop()        - Sets <item> to the last element of <list>
                                   and removes the last element from <list>
    <item> = <list>.pop(<index>) - Sets <item> to the <index> element of <list>
                                 - Removes the <index> element of <list>
    del <list>[<index>]          - Deletes the item of <list> at <index>
    <list> = []                  - Clears <list> by setting it to an empty list
    ----     ----     ----

    ---- Finding Items ----
    <list>.index(<item>) - Finds the first index of <item> in <list>
                           Returns -1 if <item> is not found
    <list>.count(<item>) - Returns the number of times <item> appears in <list>
    ----      ----     ----

    ---- Sorting List ----
    <list>.sort()          - Sorts <list>
    random.shuffle(<list>) - Randomly shuffles <list>
    ----  ----  ----  ----
# String #


'''

chessPieces = ["pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "rook", "knight", "bishop", "king", "queen", "bishop", "knight", "rook"]

pawnCount = chessPieces.count("pawn")

while pawnCount > 8:
    chessPieces.pop(chessPieces.index("pawn"))
    pawnCount = pawnCount - 1

print(chessPieces)

#### Databases ####
# C - Create
christmasList = []
groceryList = ["turkey butts", 
                   "ham", 
                   "eggnog", 
                   "sweet potato pie"]
genericList = [1 , "string", [1, "another"]]
# R - Read
# U - Update
# D - Delete

