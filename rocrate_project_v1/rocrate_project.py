# Auto generated from rocrate_project.yaml by pythongen.py version: 0.0.1
# Generation date: 2023-12-14T09:19:24
# Schema: roCrateProject
#
# id: https://example.com/ro-crate-project
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

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
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
ROP = CurieNamespace('rop', 'https://example.com/ro-crate-project')
DEFAULT_ = ROP


# Types

# Class references



@dataclass
class Project(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ROP["Project"]
    class_class_curie: ClassVar[str] = "rop:Project"
    class_name: ClassVar[str] = "Project"
    class_model_uri: ClassVar[URIRef] = ROP.Project

    name: Optional[str] = None
    description: Optional[str] = None
    identifier: Optional[str] = None
    version: Optional[str] = None
    datePublished: Optional[str] = None
    license: Optional[str] = None
    keywords: Optional[str] = None
    url: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if self.datePublished is not None and not isinstance(self.datePublished, str):
            self.datePublished = str(self.datePublished)

        if self.license is not None and not isinstance(self.license, str):
            self.license = str(self.license)

        if self.keywords is not None and not isinstance(self.keywords, str):
            self.keywords = str(self.keywords)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.project__name = Slot(uri=ROP.name, name="project__name", curie=ROP.curie('name'),
                   model_uri=ROP.project__name, domain=None, range=Optional[str])

slots.project__description = Slot(uri=ROP.description, name="project__description", curie=ROP.curie('description'),
                   model_uri=ROP.project__description, domain=None, range=Optional[str])

slots.project__identifier = Slot(uri=ROP.identifier, name="project__identifier", curie=ROP.curie('identifier'),
                   model_uri=ROP.project__identifier, domain=None, range=Optional[str])

slots.project__version = Slot(uri=ROP.version, name="project__version", curie=ROP.curie('version'),
                   model_uri=ROP.project__version, domain=None, range=Optional[str])

slots.project__datePublished = Slot(uri=ROP.datePublished, name="project__datePublished", curie=ROP.curie('datePublished'),
                   model_uri=ROP.project__datePublished, domain=None, range=Optional[str])

slots.project__license = Slot(uri=ROP.license, name="project__license", curie=ROP.curie('license'),
                   model_uri=ROP.project__license, domain=None, range=Optional[str])

slots.project__keywords = Slot(uri=ROP.keywords, name="project__keywords", curie=ROP.curie('keywords'),
                   model_uri=ROP.project__keywords, domain=None, range=Optional[str])

slots.project__url = Slot(uri=ROP.url, name="project__url", curie=ROP.curie('url'),
                   model_uri=ROP.project__url, domain=None, range=Optional[str])
