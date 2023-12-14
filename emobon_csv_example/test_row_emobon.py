# Auto generated from test_csv_row.yaml by pythongen.py version: 0.0.1
# Generation date: 2023-12-14T15:43:18
# Schema: DataModel
#
# id: https://example.com/data
# description:
# license:

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace


metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'https://example.com/data')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = SCHEMA


# Types
class String(str):
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "string"
    type_model_uri = SCHEMA.String


class Integer(int):
    type_class_uri = XSD["integer"]
    type_class_curie = "xsd:integer"
    type_name = "integer"
    type_model_uri = SCHEMA.Integer


class Float(float):
    type_class_uri = XSD["float"]
    type_class_curie = "xsd:float"
    type_name = "float"
    type_model_uri = SCHEMA.Float


# Class references



@dataclass
class DataRow(YAMLRoot):
    """
    A row of data
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["DataRow"]
    class_class_curie: ClassVar[str] = "schema:DataRow"
    class_name: ClassVar[str] = "DataRow"
    class_model_uri: ClassVar[URIRef] = SCHEMA.DataRow

    source_mat_id: str = None
    sea_surf_temp: Optional[float] = None
    sea_surf_temp_method: Optional[str] = None
    ph: Optional[float] = None
    ph_method: Optional[str] = None
    sediment_temp: Optional[float] = None
    sediment_temp_method: Optional[str] = None
    redox_potential: Optional[float] = None
    redox_potential_method: Optional[str] = None
    alkalinity: Optional[float] = None
    alkalinity_method: Optional[str] = None
    ammonium: Optional[float] = None
    ammonium_method: Optional[str] = None
    bac_prod: Optional[float] = None
    bac_prod_method: Optional[str] = None
    biomass: Optional[float] = None
    biomass_method: Optional[str] = None
    chem_administration: Optional[str] = None
    chlorophyll: Optional[float] = None
    chlorophyll_method: Optional[str] = None
    diss_carb_dioxide: Optional[float] = None
    diss_carb_dioxide_method: Optional[str] = None
    diss_inorg_carb: Optional[float] = None
    diss_inorg_carb_method: Optional[str] = None
    diss_org_carb: Optional[float] = None
    diss_org_carb_method: Optional[str] = None
    diss_org_nitro: Optional[float] = None
    diss_org_nitro_method: Optional[str] = None
    diss_oxygen: Optional[float] = None
    diss_oxygen_method: Optional[str] = None
    magnesium: Optional[float] = None
    magnesium_method: Optional[str] = None
    methane: Optional[float] = None
    methane_method: Optional[str] = None
    n_alkanes: Optional[float] = None
    n_alkanes_method: Optional[str] = None
    nitrate: Optional[float] = None
    nitrate_method: Optional[str] = None
    nitrite: Optional[float] = None
    nitrite_method: Optional[str] = None
    organism_count: Optional[float] = None
    organism_count_method: Optional[str] = None
    oxy_stat_samp: Optional[str] = None
    part_org_carb: Optional[float] = None
    part_org_carb_method: Optional[str] = None
    part_org_nitro: Optional[float] = None
    part_org_nitro_method: Optional[str] = None
    particle_class: Optional[str] = None
    petroleum_hydrocarb: Optional[float] = None
    petroleum_hydrocarb_method: Optional[str] = None
    phaeopigments: Optional[float] = None
    phaeopigments_method: Optional[str] = None
    phosphate: Optional[float] = None
    phosphate_method: Optional[str] = None
    pigments: Optional[float] = None
    pigments_method: Optional[str] = None
    porosity: Optional[float] = None
    pressure: Optional[float] = None
    pressure_method: Optional[str] = None
    sea_surf_salinity: Optional[float] = None
    sea_surf_salinity_method: Optional[str] = None
    silicate: Optional[float] = None
    silicate_method: Optional[str] = None
    sulfate: Optional[float] = None
    sulfate_method: Optional[str] = None
    sulfide: Optional[float] = None
    sulfide_method: Optional[str] = None
    water_current: Optional[float] = None
    water_current_method: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.source_mat_id):
            self.MissingRequiredField("source_mat_id")
        if not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        if self.sea_surf_temp is not None and not isinstance(self.sea_surf_temp, float):
            self.sea_surf_temp = float(self.sea_surf_temp)

        if self.sea_surf_temp_method is not None and not isinstance(self.sea_surf_temp_method, str):
            self.sea_surf_temp_method = str(self.sea_surf_temp_method)

        if self.ph is not None and not isinstance(self.ph, float):
            self.ph = float(self.ph)

        if self.ph_method is not None and not isinstance(self.ph_method, str):
            self.ph_method = str(self.ph_method)

        if self.sediment_temp is not None and not isinstance(self.sediment_temp, float):
            self.sediment_temp = float(self.sediment_temp)

        if self.sediment_temp_method is not None and not isinstance(self.sediment_temp_method, str):
            self.sediment_temp_method = str(self.sediment_temp_method)

        if self.redox_potential is not None and not isinstance(self.redox_potential, float):
            self.redox_potential = float(self.redox_potential)

        if self.redox_potential_method is not None and not isinstance(self.redox_potential_method, str):
            self.redox_potential_method = str(self.redox_potential_method)

        if self.alkalinity is not None and not isinstance(self.alkalinity, float):
            self.alkalinity = float(self.alkalinity)

        if self.alkalinity_method is not None and not isinstance(self.alkalinity_method, str):
            self.alkalinity_method = str(self.alkalinity_method)

        if self.ammonium is not None and not isinstance(self.ammonium, float):
            self.ammonium = float(self.ammonium)

        if self.ammonium_method is not None and not isinstance(self.ammonium_method, str):
            self.ammonium_method = str(self.ammonium_method)

        if self.bac_prod is not None and not isinstance(self.bac_prod, float):
            self.bac_prod = float(self.bac_prod)

        if self.bac_prod_method is not None and not isinstance(self.bac_prod_method, str):
            self.bac_prod_method = str(self.bac_prod_method)

        if self.biomass is not None and not isinstance(self.biomass, float):
            self.biomass = float(self.biomass)

        if self.biomass_method is not None and not isinstance(self.biomass_method, str):
            self.biomass_method = str(self.biomass_method)

        if self.chem_administration is not None and not isinstance(self.chem_administration, str):
            self.chem_administration = str(self.chem_administration)

        if self.chlorophyll is not None and not isinstance(self.chlorophyll, float):
            self.chlorophyll = float(self.chlorophyll)

        if self.chlorophyll_method is not None and not isinstance(self.chlorophyll_method, str):
            self.chlorophyll_method = str(self.chlorophyll_method)

        if self.diss_carb_dioxide is not None and not isinstance(self.diss_carb_dioxide, float):
            self.diss_carb_dioxide = float(self.diss_carb_dioxide)

        if self.diss_carb_dioxide_method is not None and not isinstance(self.diss_carb_dioxide_method, str):
            self.diss_carb_dioxide_method = str(self.diss_carb_dioxide_method)

        if self.diss_inorg_carb is not None and not isinstance(self.diss_inorg_carb, float):
            self.diss_inorg_carb = float(self.diss_inorg_carb)

        if self.diss_inorg_carb_method is not None and not isinstance(self.diss_inorg_carb_method, str):
            self.diss_inorg_carb_method = str(self.diss_inorg_carb_method)

        if self.diss_org_carb is not None and not isinstance(self.diss_org_carb, float):
            self.diss_org_carb = float(self.diss_org_carb)

        if self.diss_org_carb_method is not None and not isinstance(self.diss_org_carb_method, str):
            self.diss_org_carb_method = str(self.diss_org_carb_method)

        if self.diss_org_nitro is not None and not isinstance(self.diss_org_nitro, float):
            self.diss_org_nitro = float(self.diss_org_nitro)

        if self.diss_org_nitro_method is not None and not isinstance(self.diss_org_nitro_method, str):
            self.diss_org_nitro_method = str(self.diss_org_nitro_method)

        if self.diss_oxygen is not None and not isinstance(self.diss_oxygen, float):
            self.diss_oxygen = float(self.diss_oxygen)

        if self.diss_oxygen_method is not None and not isinstance(self.diss_oxygen_method, str):
            self.diss_oxygen_method = str(self.diss_oxygen_method)

        if self.magnesium is not None and not isinstance(self.magnesium, float):
            self.magnesium = float(self.magnesium)

        if self.magnesium_method is not None and not isinstance(self.magnesium_method, str):
            self.magnesium_method = str(self.magnesium_method)

        if self.methane is not None and not isinstance(self.methane, float):
            self.methane = float(self.methane)

        if self.methane_method is not None and not isinstance(self.methane_method, str):
            self.methane_method = str(self.methane_method)

        if self.n_alkanes is not None and not isinstance(self.n_alkanes, float):
            self.n_alkanes = float(self.n_alkanes)

        if self.n_alkanes_method is not None and not isinstance(self.n_alkanes_method, str):
            self.n_alkanes_method = str(self.n_alkanes_method)

        if self.nitrate is not None and not isinstance(self.nitrate, float):
            self.nitrate = float(self.nitrate)

        if self.nitrate_method is not None and not isinstance(self.nitrate_method, str):
            self.nitrate_method = str(self.nitrate_method)

        if self.nitrite is not None and not isinstance(self.nitrite, float):
            self.nitrite = float(self.nitrite)

        if self.nitrite_method is not None and not isinstance(self.nitrite_method, str):
            self.nitrite_method = str(self.nitrite_method)

        if self.organism_count is not None and not isinstance(self.organism_count, float):
            self.organism_count = float(self.organism_count)

        if self.organism_count_method is not None and not isinstance(self.organism_count_method, str):
            self.organism_count_method = str(self.organism_count_method)

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, str):
            self.oxy_stat_samp = str(self.oxy_stat_samp)

        if self.part_org_carb is not None and not isinstance(self.part_org_carb, float):
            self.part_org_carb = float(self.part_org_carb)

        if self.part_org_carb_method is not None and not isinstance(self.part_org_carb_method, str):
            self.part_org_carb_method = str(self.part_org_carb_method)

        if self.part_org_nitro is not None and not isinstance(self.part_org_nitro, float):
            self.part_org_nitro = float(self.part_org_nitro)

        if self.part_org_nitro_method is not None and not isinstance(self.part_org_nitro_method, str):
            self.part_org_nitro_method = str(self.part_org_nitro_method)

        if self.particle_class is not None and not isinstance(self.particle_class, str):
            self.particle_class = str(self.particle_class)

        if self.petroleum_hydrocarb is not None and not isinstance(self.petroleum_hydrocarb, float):
            self.petroleum_hydrocarb = float(self.petroleum_hydrocarb)

        if self.petroleum_hydrocarb_method is not None and not isinstance(self.petroleum_hydrocarb_method, str):
            self.petroleum_hydrocarb_method = str(self.petroleum_hydrocarb_method)

        if self.phaeopigments is not None and not isinstance(self.phaeopigments, float):
            self.phaeopigments = float(self.phaeopigments)

        if self.phaeopigments_method is not None and not isinstance(self.phaeopigments_method, str):
            self.phaeopigments_method = str(self.phaeopigments_method)

        if self.phosphate is not None and not isinstance(self.phosphate, float):
            self.phosphate = float(self.phosphate)

        if self.phosphate_method is not None and not isinstance(self.phosphate_method, str):
            self.phosphate_method = str(self.phosphate_method)

        if self.pigments is not None and not isinstance(self.pigments, float):
            self.pigments = float(self.pigments)

        if self.pigments_method is not None and not isinstance(self.pigments_method, str):
            self.pigments_method = str(self.pigments_method)

        if self.porosity is not None and not isinstance(self.porosity, float):
            self.porosity = float(self.porosity)

        if self.pressure is not None and not isinstance(self.pressure, float):
            self.pressure = float(self.pressure)

        if self.pressure_method is not None and not isinstance(self.pressure_method, str):
            self.pressure_method = str(self.pressure_method)

        if self.sea_surf_salinity is not None and not isinstance(self.sea_surf_salinity, float):
            self.sea_surf_salinity = float(self.sea_surf_salinity)

        if self.sea_surf_salinity_method is not None and not isinstance(self.sea_surf_salinity_method, str):
            self.sea_surf_salinity_method = str(self.sea_surf_salinity_method)

        if self.silicate is not None and not isinstance(self.silicate, float):
            self.silicate = float(self.silicate)

        if self.silicate_method is not None and not isinstance(self.silicate_method, str):
            self.silicate_method = str(self.silicate_method)

        if self.sulfate is not None and not isinstance(self.sulfate, float):
            self.sulfate = float(self.sulfate)

        if self.sulfate_method is not None and not isinstance(self.sulfate_method, str):
            self.sulfate_method = str(self.sulfate_method)

        if self.sulfide is not None and not isinstance(self.sulfide, float):
            self.sulfide = float(self.sulfide)

        if self.sulfide_method is not None and not isinstance(self.sulfide_method, str):
            self.sulfide_method = str(self.sulfide_method)

        if self.water_current is not None and not isinstance(self.water_current, float):
            self.water_current = float(self.water_current)

        if self.water_current_method is not None and not isinstance(self.water_current_method, str):
            self.water_current_method = str(self.water_current_method)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.source_mat_id = Slot(uri=SCHEMA.source_mat_id, name="source_mat_id", curie=SCHEMA.curie('source_mat_id'),
                   model_uri=SCHEMA.source_mat_id, domain=None, range=str,
                   pattern=re.compile(r'^EMOBON_BPNS_So_\d{6}_[a-z_]+[0-9a-z]+$'))

slots.sea_surf_temp = Slot(uri=SCHEMA.sea_surf_temp, name="sea_surf_temp", curie=SCHEMA.curie('sea_surf_temp'),
                   model_uri=SCHEMA.sea_surf_temp, domain=None, range=Optional[float])

slots.sea_surf_temp_method = Slot(uri=SCHEMA.sea_surf_temp_method, name="sea_surf_temp_method", curie=SCHEMA.curie('sea_surf_temp_method'),
                   model_uri=SCHEMA.sea_surf_temp_method, domain=None, range=Optional[str])

slots.ph = Slot(uri=SCHEMA.ph, name="ph", curie=SCHEMA.curie('ph'),
                   model_uri=SCHEMA.ph, domain=None, range=Optional[float])

slots.ph_method = Slot(uri=SCHEMA.ph_method, name="ph_method", curie=SCHEMA.curie('ph_method'),
                   model_uri=SCHEMA.ph_method, domain=None, range=Optional[str])

slots.sediment_temp = Slot(uri=SCHEMA.sediment_temp, name="sediment_temp", curie=SCHEMA.curie('sediment_temp'),
                   model_uri=SCHEMA.sediment_temp, domain=None, range=Optional[float])

slots.sediment_temp_method = Slot(uri=SCHEMA.sediment_temp_method, name="sediment_temp_method", curie=SCHEMA.curie('sediment_temp_method'),
                   model_uri=SCHEMA.sediment_temp_method, domain=None, range=Optional[str])

slots.redox_potential = Slot(uri=SCHEMA.redox_potential, name="redox_potential", curie=SCHEMA.curie('redox_potential'),
                   model_uri=SCHEMA.redox_potential, domain=None, range=Optional[float])

slots.redox_potential_method = Slot(uri=SCHEMA.redox_potential_method, name="redox_potential_method", curie=SCHEMA.curie('redox_potential_method'),
                   model_uri=SCHEMA.redox_potential_method, domain=None, range=Optional[str])

slots.alkalinity = Slot(uri=SCHEMA.alkalinity, name="alkalinity", curie=SCHEMA.curie('alkalinity'),
                   model_uri=SCHEMA.alkalinity, domain=None, range=Optional[float])

slots.alkalinity_method = Slot(uri=SCHEMA.alkalinity_method, name="alkalinity_method", curie=SCHEMA.curie('alkalinity_method'),
                   model_uri=SCHEMA.alkalinity_method, domain=None, range=Optional[str])

slots.ammonium = Slot(uri=SCHEMA.ammonium, name="ammonium", curie=SCHEMA.curie('ammonium'),
                   model_uri=SCHEMA.ammonium, domain=None, range=Optional[float])

slots.ammonium_method = Slot(uri=SCHEMA.ammonium_method, name="ammonium_method", curie=SCHEMA.curie('ammonium_method'),
                   model_uri=SCHEMA.ammonium_method, domain=None, range=Optional[str])

slots.bac_prod = Slot(uri=SCHEMA.bac_prod, name="bac_prod", curie=SCHEMA.curie('bac_prod'),
                   model_uri=SCHEMA.bac_prod, domain=None, range=Optional[float])

slots.bac_prod_method = Slot(uri=SCHEMA.bac_prod_method, name="bac_prod_method", curie=SCHEMA.curie('bac_prod_method'),
                   model_uri=SCHEMA.bac_prod_method, domain=None, range=Optional[str])

slots.biomass = Slot(uri=SCHEMA.biomass, name="biomass", curie=SCHEMA.curie('biomass'),
                   model_uri=SCHEMA.biomass, domain=None, range=Optional[float])

slots.biomass_method = Slot(uri=SCHEMA.biomass_method, name="biomass_method", curie=SCHEMA.curie('biomass_method'),
                   model_uri=SCHEMA.biomass_method, domain=None, range=Optional[str])

slots.chem_administration = Slot(uri=SCHEMA.chem_administration, name="chem_administration", curie=SCHEMA.curie('chem_administration'),
                   model_uri=SCHEMA.chem_administration, domain=None, range=Optional[str])

slots.chlorophyll = Slot(uri=SCHEMA.chlorophyll, name="chlorophyll", curie=SCHEMA.curie('chlorophyll'),
                   model_uri=SCHEMA.chlorophyll, domain=None, range=Optional[float])

slots.chlorophyll_method = Slot(uri=SCHEMA.chlorophyll_method, name="chlorophyll_method", curie=SCHEMA.curie('chlorophyll_method'),
                   model_uri=SCHEMA.chlorophyll_method, domain=None, range=Optional[str])

slots.diss_carb_dioxide = Slot(uri=SCHEMA.diss_carb_dioxide, name="diss_carb_dioxide", curie=SCHEMA.curie('diss_carb_dioxide'),
                   model_uri=SCHEMA.diss_carb_dioxide, domain=None, range=Optional[float])

slots.diss_carb_dioxide_method = Slot(uri=SCHEMA.diss_carb_dioxide_method, name="diss_carb_dioxide_method", curie=SCHEMA.curie('diss_carb_dioxide_method'),
                   model_uri=SCHEMA.diss_carb_dioxide_method, domain=None, range=Optional[str])

slots.diss_inorg_carb = Slot(uri=SCHEMA.diss_inorg_carb, name="diss_inorg_carb", curie=SCHEMA.curie('diss_inorg_carb'),
                   model_uri=SCHEMA.diss_inorg_carb, domain=None, range=Optional[float])

slots.diss_inorg_carb_method = Slot(uri=SCHEMA.diss_inorg_carb_method, name="diss_inorg_carb_method", curie=SCHEMA.curie('diss_inorg_carb_method'),
                   model_uri=SCHEMA.diss_inorg_carb_method, domain=None, range=Optional[str])

slots.diss_org_carb = Slot(uri=SCHEMA.diss_org_carb, name="diss_org_carb", curie=SCHEMA.curie('diss_org_carb'),
                   model_uri=SCHEMA.diss_org_carb, domain=None, range=Optional[float])

slots.diss_org_carb_method = Slot(uri=SCHEMA.diss_org_carb_method, name="diss_org_carb_method", curie=SCHEMA.curie('diss_org_carb_method'),
                   model_uri=SCHEMA.diss_org_carb_method, domain=None, range=Optional[str])

slots.diss_org_nitro = Slot(uri=SCHEMA.diss_org_nitro, name="diss_org_nitro", curie=SCHEMA.curie('diss_org_nitro'),
                   model_uri=SCHEMA.diss_org_nitro, domain=None, range=Optional[float])

slots.diss_org_nitro_method = Slot(uri=SCHEMA.diss_org_nitro_method, name="diss_org_nitro_method", curie=SCHEMA.curie('diss_org_nitro_method'),
                   model_uri=SCHEMA.diss_org_nitro_method, domain=None, range=Optional[str])

slots.diss_oxygen = Slot(uri=SCHEMA.diss_oxygen, name="diss_oxygen", curie=SCHEMA.curie('diss_oxygen'),
                   model_uri=SCHEMA.diss_oxygen, domain=None, range=Optional[float])

slots.diss_oxygen_method = Slot(uri=SCHEMA.diss_oxygen_method, name="diss_oxygen_method", curie=SCHEMA.curie('diss_oxygen_method'),
                   model_uri=SCHEMA.diss_oxygen_method, domain=None, range=Optional[str])

slots.magnesium = Slot(uri=SCHEMA.magnesium, name="magnesium", curie=SCHEMA.curie('magnesium'),
                   model_uri=SCHEMA.magnesium, domain=None, range=Optional[float])

slots.magnesium_method = Slot(uri=SCHEMA.magnesium_method, name="magnesium_method", curie=SCHEMA.curie('magnesium_method'),
                   model_uri=SCHEMA.magnesium_method, domain=None, range=Optional[str])

slots.methane = Slot(uri=SCHEMA.methane, name="methane", curie=SCHEMA.curie('methane'),
                   model_uri=SCHEMA.methane, domain=None, range=Optional[float])

slots.methane_method = Slot(uri=SCHEMA.methane_method, name="methane_method", curie=SCHEMA.curie('methane_method'),
                   model_uri=SCHEMA.methane_method, domain=None, range=Optional[str])

slots.n_alkanes = Slot(uri=SCHEMA.n_alkanes, name="n_alkanes", curie=SCHEMA.curie('n_alkanes'),
                   model_uri=SCHEMA.n_alkanes, domain=None, range=Optional[float])

slots.n_alkanes_method = Slot(uri=SCHEMA.n_alkanes_method, name="n_alkanes_method", curie=SCHEMA.curie('n_alkanes_method'),
                   model_uri=SCHEMA.n_alkanes_method, domain=None, range=Optional[str])

slots.nitrate = Slot(uri=SCHEMA.nitrate, name="nitrate", curie=SCHEMA.curie('nitrate'),
                   model_uri=SCHEMA.nitrate, domain=None, range=Optional[float])

slots.nitrate_method = Slot(uri=SCHEMA.nitrate_method, name="nitrate_method", curie=SCHEMA.curie('nitrate_method'),
                   model_uri=SCHEMA.nitrate_method, domain=None, range=Optional[str])

slots.nitrite = Slot(uri=SCHEMA.nitrite, name="nitrite", curie=SCHEMA.curie('nitrite'),
                   model_uri=SCHEMA.nitrite, domain=None, range=Optional[float])

slots.nitrite_method = Slot(uri=SCHEMA.nitrite_method, name="nitrite_method", curie=SCHEMA.curie('nitrite_method'),
                   model_uri=SCHEMA.nitrite_method, domain=None, range=Optional[str])

slots.organism_count = Slot(uri=SCHEMA.organism_count, name="organism_count", curie=SCHEMA.curie('organism_count'),
                   model_uri=SCHEMA.organism_count, domain=None, range=Optional[float])

slots.organism_count_method = Slot(uri=SCHEMA.organism_count_method, name="organism_count_method", curie=SCHEMA.curie('organism_count_method'),
                   model_uri=SCHEMA.organism_count_method, domain=None, range=Optional[str])

slots.oxy_stat_samp = Slot(uri=SCHEMA.oxy_stat_samp, name="oxy_stat_samp", curie=SCHEMA.curie('oxy_stat_samp'),
                   model_uri=SCHEMA.oxy_stat_samp, domain=None, range=Optional[str])

slots.part_org_carb = Slot(uri=SCHEMA.part_org_carb, name="part_org_carb", curie=SCHEMA.curie('part_org_carb'),
                   model_uri=SCHEMA.part_org_carb, domain=None, range=Optional[float])

slots.part_org_carb_method = Slot(uri=SCHEMA.part_org_carb_method, name="part_org_carb_method", curie=SCHEMA.curie('part_org_carb_method'),
                   model_uri=SCHEMA.part_org_carb_method, domain=None, range=Optional[str])

slots.part_org_nitro = Slot(uri=SCHEMA.part_org_nitro, name="part_org_nitro", curie=SCHEMA.curie('part_org_nitro'),
                   model_uri=SCHEMA.part_org_nitro, domain=None, range=Optional[float])

slots.part_org_nitro_method = Slot(uri=SCHEMA.part_org_nitro_method, name="part_org_nitro_method", curie=SCHEMA.curie('part_org_nitro_method'),
                   model_uri=SCHEMA.part_org_nitro_method, domain=None, range=Optional[str])

slots.particle_class = Slot(uri=SCHEMA.particle_class, name="particle_class", curie=SCHEMA.curie('particle_class'),
                   model_uri=SCHEMA.particle_class, domain=None, range=Optional[str])

slots.petroleum_hydrocarb = Slot(uri=SCHEMA.petroleum_hydrocarb, name="petroleum_hydrocarb", curie=SCHEMA.curie('petroleum_hydrocarb'),
                   model_uri=SCHEMA.petroleum_hydrocarb, domain=None, range=Optional[float])

slots.petroleum_hydrocarb_method = Slot(uri=SCHEMA.petroleum_hydrocarb_method, name="petroleum_hydrocarb_method", curie=SCHEMA.curie('petroleum_hydrocarb_method'),
                   model_uri=SCHEMA.petroleum_hydrocarb_method, domain=None, range=Optional[str])

slots.phaeopigments = Slot(uri=SCHEMA.phaeopigments, name="phaeopigments", curie=SCHEMA.curie('phaeopigments'),
                   model_uri=SCHEMA.phaeopigments, domain=None, range=Optional[float])

slots.phaeopigments_method = Slot(uri=SCHEMA.phaeopigments_method, name="phaeopigments_method", curie=SCHEMA.curie('phaeopigments_method'),
                   model_uri=SCHEMA.phaeopigments_method, domain=None, range=Optional[str])

slots.phosphate = Slot(uri=SCHEMA.phosphate, name="phosphate", curie=SCHEMA.curie('phosphate'),
                   model_uri=SCHEMA.phosphate, domain=None, range=Optional[float])

slots.phosphate_method = Slot(uri=SCHEMA.phosphate_method, name="phosphate_method", curie=SCHEMA.curie('phosphate_method'),
                   model_uri=SCHEMA.phosphate_method, domain=None, range=Optional[str])

slots.pigments = Slot(uri=SCHEMA.pigments, name="pigments", curie=SCHEMA.curie('pigments'),
                   model_uri=SCHEMA.pigments, domain=None, range=Optional[float])

slots.pigments_method = Slot(uri=SCHEMA.pigments_method, name="pigments_method", curie=SCHEMA.curie('pigments_method'),
                   model_uri=SCHEMA.pigments_method, domain=None, range=Optional[str])

slots.porosity = Slot(uri=SCHEMA.porosity, name="porosity", curie=SCHEMA.curie('porosity'),
                   model_uri=SCHEMA.porosity, domain=None, range=Optional[float])

slots.pressure = Slot(uri=SCHEMA.pressure, name="pressure", curie=SCHEMA.curie('pressure'),
                   model_uri=SCHEMA.pressure, domain=None, range=Optional[float])

slots.pressure_method = Slot(uri=SCHEMA.pressure_method, name="pressure_method", curie=SCHEMA.curie('pressure_method'),
                   model_uri=SCHEMA.pressure_method, domain=None, range=Optional[str])

slots.sea_surf_salinity = Slot(uri=SCHEMA.sea_surf_salinity, name="sea_surf_salinity", curie=SCHEMA.curie('sea_surf_salinity'),
                   model_uri=SCHEMA.sea_surf_salinity, domain=None, range=Optional[float])

slots.sea_surf_salinity_method = Slot(uri=SCHEMA.sea_surf_salinity_method, name="sea_surf_salinity_method", curie=SCHEMA.curie('sea_surf_salinity_method'),
                   model_uri=SCHEMA.sea_surf_salinity_method, domain=None, range=Optional[str])

slots.silicate = Slot(uri=SCHEMA.silicate, name="silicate", curie=SCHEMA.curie('silicate'),
                   model_uri=SCHEMA.silicate, domain=None, range=Optional[float])

slots.silicate_method = Slot(uri=SCHEMA.silicate_method, name="silicate_method", curie=SCHEMA.curie('silicate_method'),
                   model_uri=SCHEMA.silicate_method, domain=None, range=Optional[str])

slots.sulfate = Slot(uri=SCHEMA.sulfate, name="sulfate", curie=SCHEMA.curie('sulfate'),
                   model_uri=SCHEMA.sulfate, domain=None, range=Optional[float])

slots.sulfate_method = Slot(uri=SCHEMA.sulfate_method, name="sulfate_method", curie=SCHEMA.curie('sulfate_method'),
                   model_uri=SCHEMA.sulfate_method, domain=None, range=Optional[str])

slots.sulfide = Slot(uri=SCHEMA.sulfide, name="sulfide", curie=SCHEMA.curie('sulfide'),
                   model_uri=SCHEMA.sulfide, domain=None, range=Optional[float])

slots.sulfide_method = Slot(uri=SCHEMA.sulfide_method, name="sulfide_method", curie=SCHEMA.curie('sulfide_method'),
                   model_uri=SCHEMA.sulfide_method, domain=None, range=Optional[str])

slots.water_current = Slot(uri=SCHEMA.water_current, name="water_current", curie=SCHEMA.curie('water_current'),
                   model_uri=SCHEMA.water_current, domain=None, range=Optional[float])

slots.water_current_method = Slot(uri=SCHEMA.water_current_method, name="water_current_method", curie=SCHEMA.curie('water_current_method'),
                   model_uri=SCHEMA.water_current_method, domain=None, range=Optional[str])
