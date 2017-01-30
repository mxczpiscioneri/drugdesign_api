import json
from classes.ResultMolecule import ResultMolecule
from classes.SelectedParametersResults import SelectedParametersResults

with open("result.json") as json_file:
    data = json.load(json_file)

    # ---------- Energy -------------------------------
    # Molecules
    results_energy = data["energy"]["results"]
    allResultMoleculeEnergy = []
    for dic in results_energy:
        resultMoleculeEnergy = ResultMolecule()
        resultMoleculeEnergy.dic2obj(dic)
        allResultMoleculeEnergy.append(resultMoleculeEnergy)
    #print all molecules
    for resultMoleculeEnergy in allResultMoleculeEnergy:
        resultMoleculeEnergy.printAll()

    # Residues
    residues_energy = data["energy"]["residues"]
    SelectedParametersResultsEnergy = SelectedParametersResults()
    SelectedParametersResultsEnergy.setResidues(residues_energy)
    SelectedParametersResultsEnergy.printAll()
# -----------------------------------------------------

    # ---------- Hydrogen -------------------------------
    # Molecules
    results_hydrogen = data["hydrogen"]["results"]
    allResultMoleculeHydrogen = []
    for dic in results_hydrogen:
        resultMoleculeHydrogen = ResultMolecule()
        resultMoleculeHydrogen.dic2obj(dic)
        allResultMoleculeHydrogen.append(resultMoleculeHydrogen)
    #print all molecules
    for resultMoleculeHydrogen in allResultMoleculeHydrogen:
        resultMoleculeHydrogen.printAll()

    # Residues
    residues_hydrogen = data["hydrogen"]["residues"]
    SelectedParametersResultsHydrogen = SelectedParametersResults()
    SelectedParametersResultsHydrogen.setResidues(residues_hydrogen)
    SelectedParametersResultsHydrogen.printAll()
# -----------------------------------------------------