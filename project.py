from Bio.Seq import Seq
sequence = Seq("ATCGTAGCTA")
print("Sequence:", sequence)
print("Complement:", sequence.complement())
print("Reverse complement:", sequence.reverse_complement())