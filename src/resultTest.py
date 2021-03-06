import json
from classes.ResultMolecule import ResultMolecule
from classes.SelectedParametersResults import SelectedParametersResults

with open("result.json") as json_file:
    data = json.load(json_file)

    # ---------- Energy -------------------------------
    results_energy = data["energy"]["results"]
    vs_id_energy = data["energy"]["vsId"]
    residues_energy = data["energy"]["residues"]
    range_energy_min = data["energy"]["rangeMin"]
    range_energy_max = data["energy"]["rangeMax"]

    selectedParametersEnergy = SelectedParametersResults(vs_id_energy)
    selectedParametersEnergy.setResidues(residues_energy)
    selectedParametersEnergy.setRange(range_energy_min, range_energy_max)
    selectedParametersEnergy.setOption("energy")
    selectedParametersEnergy.printAll()

    # Molecules
    allResultMoleculeEnergy = []
    for dic in results_energy:
        resultMoleculeEnergy = ResultMolecule(vs_id_energy)
        resultMoleculeEnergy.dic2obj(dic)
        allResultMoleculeEnergy.append(resultMoleculeEnergy)
    #print all molecules
    for resultMoleculeEnergy in allResultMoleculeEnergy:
        resultMoleculeEnergy.printAll()
# -----------------------------------------------------


    # ---------- Hydrogen -------------------------------
    results_hydrogen = data["hydrogen"]["results"]
    vs_id_hydrogen = data["hydrogen"]["vsId"]
    residues_hydrogen = data["hydrogen"]["residues"]
    range_hydrogen_min = data["hydrogen"]["rangeMin"]
    range_hydrogen_max = data["hydrogen"]["rangeMax"]

    selectedParametersHydrogen = SelectedParametersResults(vs_id_hydrogen)
    selectedParametersHydrogen.setResidues(residues_hydrogen)
    selectedParametersHydrogen.setRange(range_hydrogen_min, range_hydrogen_max)
    selectedParametersHydrogen.setOption("hydrogen")
    selectedParametersHydrogen.printAll()

    # Molecules
    allResultMoleculeHydrogen = []
    for dic in results_hydrogen:
        resultMoleculeHydrogen = ResultMolecule(vs_id_hydrogen)
        resultMoleculeHydrogen.dic2obj(dic)
        allResultMoleculeHydrogen.append(resultMoleculeHydrogen)
    #print all molecules
    for resultMoleculeHydrogen in allResultMoleculeHydrogen:
        resultMoleculeHydrogen.printAll()
# -----------------------------------------------------
