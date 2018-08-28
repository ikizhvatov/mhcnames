# Copyright (c) 2018. Mount Sinai School of Medicine
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function, division, absolute_import

from .locus import Locus

class AlleleGroup(Locus):
    """
    Representation of a group of closely related alleles,
    specified by a species, a gene, and a group identifier,
    such as "HLA-A*02".

    These are not the same as serotypes (e.g. HLA-A2). Serotypes
    correspond to a group of proteins which can all be identified with
    the same antibody. Allele groups in modern MHC nomenclature
    are closely related but not every allele in a group is also
    in the similarly named serotype (and vice versa).
    """
    def __init__(self, species_prefix, gene_name, group_id):
        Locus.__init__(self, species_prefix, gene_name)
        self.group_id = group_id

    def normalized_string(self, include_species=True):
        return "%s*%s" % (
            Locus.normalized_string(self, include_species=include_species),
            self.group_id)

    def compact_string(self, include_species=True):
        """
        Compact representation of an AlleleGroup, omits the "*"
        in an allele group.
            Normalized: HLA-A*02
            Compact: HLA-A02
        """
        return "%s%s" % (
            Locus.compact_string(include_species=include_species),
            self.group_id)

    def to_allele_group(self):
        """
        For AlleleGroup objects this acts as a simple copy but descendant
        classes use this method to project their fields down to a AlleleGroup
        object.
        """
        return AlleleGroup(self.species_prefix, self.gene_name, self.group_id)

    def to_dict(self):
        """
        Returns dictionary with all fields of this allele group,
        as well as its representations as a locus.
        """
        d = Locus.to_dict(self)
        d["allele_group"] = self.normalized_string()
        d["group_id"] = self.group_id
        return d
