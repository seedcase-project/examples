import seedcase_sprout.core as sp
import os
import pathlib

os.environ["SPROUT_GLOBAL"] = "./male-seed-beetle"

package_paths = sp.create_package_structure(path=sp.path_packages())

properties = sp.PackageProperties(
    name="male-seed-beetle",
    title="Complex mitonuclear interactions and metabolic costs of mating in male seed beetles",
    description="Data from the 2015 on metabolic rate, respiratory quotient, body weight and ejaculate weight data from seed beetles with different mitonuclear genotypes.",
    contributors=[
        sp.ContributorProperties(
            title="Jane Doe Test",
            email="Jane.Doe@test.com",
            path="example.com/jamie_jones",
            roles=["creator"],
        )
    ],
    licenses=[
        sp.LicenseProperties(
            name="CCO_1.0",
            path="https://creativecommons.org/publicdomain/zero/1.0/legalcode",
            title="CCO 1.0 UNIVERSAL",
        )
    ],
)

package_properties = sp.edit_package_properties(
  path=sp.path_properties(package_id=1),
  properties=properties,
)

package_path = sp.write_package_properties(
  properties=package_properties,
  path=sp.path_properties(package_id=1)
)
