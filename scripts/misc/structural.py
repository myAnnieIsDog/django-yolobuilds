
# This dictionary uses code section as the key and a summary of the code requirement as the value.
#   key = code section, such as "R301.1.3.1"
#   value = code summary

def main(code_sections: list):
    _: dict
    print(f"2022 California Residential Code Sections:\n\t")
    for _ in code_sections:
        for key, item in _.items():
            print(f"{key}\t{item}")
    

R301_Structural_Design_Criteria = {
    "R301.1.3.1": "When any portion of any structure deviates from substantial compliance with conventional framing requirements for woodframe construction found in this code, the building official shall require the construction documents to be approved and stamped by a California licensed architect or engineer for that irregular or non-conforming portion of work.",

    "R301.1.3.2": "The building official shall require construction documents to be approved and stamped by a California licensed architect or engineer for all dwellings of woodframe construction more than two stories and basement in height.",

    "R301.1.3.3": "The building official shall require floor, wall or roof-ceiling structural elements in dwellings designed of cold-formed steel, concrete, masonry or structural insulated panels prescribed by this code to be approved and stamped by a California licensed architect or engineer.",

    "R301.1.4": "Intermodal shipping containers that are repurposed for use as buildings or structures shall be designed in accordance with the structural provisions in Section 3115 of the California Building Code.",

    "R301.2.1": "Ultimate design wind speed is 93 mph.",

    "R301.2.2": "Use Seismic Design Category D2 or engineering site analysis.",

    "R301.2.2.2": "Provide engineered design if assembly dead load exceeds the following: 15 psf Roof-Ceiling Assembly 10 psf Floor Assembly 15 psf Exterior light-frame walls 10 psf Interior light-frame walls",

    "R301.2.2.6": f"The following irregularities require engineered design (see exceptions): \n\tShear wall or braced wall offsets out of plane. \n\tFloor or roof is not laterally supported by shear walls or braced wall lines on all edges. \n\tShear wall or braced wall offsets in plane. \n\tFloor or roof opening exceeds 12 ft or 50% of the dimension. \n\tPortions of a floor level are vertically offset. \n\tWhere shear wall and braced wall lines do not occur in two perpendicular directions. \n\tWhere above grade story is wood-framed plus concrete or masonry construction. \n\tWhere slope exceeds 1V:5H and the tallest cripple wall or post and beam exceeds 7 ft.",

    "R301.2.2.7": "Wood structures exceeding 2-stories require engineered design.",

    "R301.2.2.10": "Water heaters and thermal storage units shall be anchored per Plumbing Code.",

    "R301.3": "Story heights exceeding 11-ft 7-in require engineered design.",

    "R301.4": "The actual weights of materials and construction shall be used for determining dead load with consideration for the dead load of fixed service equipment.",

    "R301.5": "The minimum uniformly distributed live load shall be as provided in Table R301.5",

    "R301.6": "The roof shall be designed for the live load indicated in Table R301.6 or the ground snow load indicated in Table R301.2, whichever is greater.",

    "R301.7": "The allowable deflection of any structural member under the live load listed in Sections R301.5 and R301.6 or wind loads determined by Section R301.2.1 shall not exceed the values in Table R301.7.",

    "R301.8": "For the purposes of this code, dimensions of lumber specified shall be deemed to be nominal dimensions unless specifically designated as actual dimensions.",

    "R317.1": "Protection of wood against decay shall be provided in the following: Distance to exposed ground:\n\t18” to joists, 12 inches to girders, 8 inches to columns.\n\tSills and sleepers on concrete.\n\tSiding/sheathing within 6” of ground, or 2” to concrete (sidewalks, etc.)\n\tBalconies, porches and similar supports exposed to weather.\n\tField cuts, notches, and holes shall be treated in the field.",

    "R317.1.3": "Enclosed framing in exterior balconies and elevated walking surfaces that are exposed to rain shall be provided with openings that provide a net-free cross-ventilation area not less than 1/150 of the area of each separate space."
}
    
R400_Foundations = {
    "R401.3": "Drain away 6 inches within 10 feet (5%)",

    "R401.4.1": "Geotechnical Evaluation: Yolo Builds Policy: Foundations for conventional light-frame construction do not require a geotechnical evaluation if a soil bearing capacity of 1500 psf is assumed.",

    "R402.2": "Concrete: use ACI 318 or ACI 332; min f′c =  2,500 psi; foundation walls require f′c = 3,000 psi (404.1.3.3.1)",

    "R403.1": "All exterior walls shall be supported on continuous concrete footings that shall be of sufficient design to accommodate all loads according to Section R301 and to transmit the resulting loads to the soil within the limitations as determined from the character of the soil. Footings shall be supported on undisturbed natural soils or engineered fill. Concrete footing shall be designed and constructed in accordance with the provisions of Section R403 or in accordance with ACI 332",

    "R403.1.2": "Continuous footings are required in Seismic Design Categories D0, D1, and D2 at all exterior walls, all bearing walls, and most braced walls",
    
    "R403.1.3": "Footings and Stem Wall Reinforcing in SDC D0, D1, and D2 placed per Fig R403.1.3.",

    "R403.1.3.1": "Vertical #4 @ 48” oc at centerline of the wall and Horizonal #4 within 12” of top and 3-4” from bottom of footing.",
    
    "R403.1.3.3": "Monopour: #4 top and bottom, or #5, or (2) #4 in middle third.\n\t Dual pour: add #3 dowels @ 48” oc with 14” into stem wall. Std hook and cover.",

    "R403.1.3.4": "Interior bearing and braced wall footings in SDC D must extend 12” below top of slab.",

    "R403.1.3.5": "Reinforcement must be grade 40, secured in place.",

    "R403.1.3.5.3": "Minimum rebar cover is 3” for footings and slabs, 1.5” for stem walls above grade.",

    "R403.1.4": "Min. exterior footing depth below undisturbed surface. Yolo Builds Policy: 18 inches required to meet R403.1.8 without a geotechnical report. Otherwise, 12 inches minimum depth.",

    "R403.1.5": "Max Slope: top = level; bottom ≤ 10%",

    "R403.1.6": "Foundation Anchorage (see also 602.11):\n\tMin ½”⌀ @ 6 ft oc; min 7” embedment; 3.5-12” from end; at least two per board;\n\ttwo-story: 4 ft oc",

    "R403.1.7": "Footings on or Adjacent to Slopes:\n\tAscending Slopes: smaller of 15 ft or H/2\n\tDescending Slopes: smaller of 40 ft or H/3",

    "R403.1.7.3": "Foundation Elevation: min 12 in plus 2% slope above drain inlet.",

    "R403.1.8": "Expansive soils, footing must be engineered or per CBO approval. Yolo Builds Policy: If no geotechnical report is provided, then assume the soil is expansive. CBO has preapproved footings for conventional light-frame construction do not require engineered footings if the footing is at a depth of at least 18 inches.",

    "R404.1.1": "Concrete Foundation Walls: Engineer design required if any hydrostatic pressure or unbalanced fill > 48” without lateral support at top or bottom.",

    "R404.1.3": "Concrete Foundation Walls: Concrete ACI 318 or 332 - f′c = 3000 min in SDC D.",

    "R404.1.3.1": "Concrete Cross Section must match Table R608.3",

    "R404.1.3.2": "Concrete foundation walls shall be laterally supported at the top and bottom.",

    "R404.1.3.2": "Stem walls not laterally supported at top.",
    "R404.1.3.3": "Concrete, Materials for Concrete, and Forms:\n\tMin f’c in SDC D is 3,000 psi",
    "R404.1.3.3.2": "Mixing and delivery per ASTM C94 or C685:\n\tMaximum aggregate: 1/5 narrowest dim and ¾ rebar clearance.",
    "R404.1.3.3.4": "Removable forms: slump shall not exceed 6 in. Stay in place shall exceed 6 inches.",
    "R404.1.3.3.5": "Work into forms: Use internal vibration for stay-in-place forms.",
    "R404.1.3.3.6": "Form materials must resist loading during pour.",
     
    "R404.1.3.3.7.1": "Reinforcement: SDC D req’s Grade 60 in stem walls.",
    "R404.1.3.3.7.2": "Reinforcement: Horizontal in center; vert within 1¼ inches from inside face of wall.",
    "R404.1.3.3.7.3": "Reinforcement: Wall openings require vert bar within 12 inches.",
    "R404.1.3.3.7.4": "Reinforcement: Bars must be supported in place; min cover is 1.5” for stem walls.",
    "R404.1.3.3.7.8": "Reinforcement: Joints must be at lateral support w/ #4 @ 24” and min 12” embed.",

    "R404.1.4.2": "	SDC D, concrete walls require Horizontal #4 @ 48” oc plus:\n\tMust support light-frame wood construction\n\tWall heights shall not exceed 8 ft\n\tUnbalanced backfill heights shall not exceed 48 in\n\tMin wall thickness is 7.5 in unless wall is max 4’-6”\n\tWhere above are exceeded and Tables R404.1.2(x) permit plain concrete, provide vert #4 @ 48 in oc",

    "R404.1.5": "Foundation wall thickness shall not be less than a supported wall.",
    "R404.1.6": "Height Above Finished Grade: at least 6”, or 4” if masonry veneer.",
    "R404.1.7": "Backfill Placement: after laterally supported and strength achieved.",

    "R404.3": "Wood Sill Plates: min 2”x 4”.",
    "R404.4": "Retaining Walls: Req engineering if > 48” or 24” w/ surcharge; slide, overturn SF = 1.5",

    "R405.1": "Drains shall be provided around concrete or masonry foundations that retain earth and enclose habitable or usable spaces located below grade.",
    "R406.1": "Waterproofing and Dampproofing...foundation walls that retain earth and enclose interior spaces and floors below grade...",

    "R407.1": "Columns: Wood Column Protection: see R317.",
    "R407.2": "Columns: Steel Column Protection: prevent corrosion.",
    "R407.3": "Columns: Structural Requirements: restrained laterally; wood 4” x 4” min; steel min 3” diameter.",

    "R408.1": "Underfloor Space: Vent 1/150, one within 3 ft of each ext corner, cover ¼” max (see exceptions, alternatives).",
    "R408.2": "Openings for Under-Floor Ventilationmust be 1/4” mesh or similar.",
    "R408.3": "Unvented Crawl Space: vapor retarder, mech exhaust, air supply, dehumidifier.",
    "R408.4": "Access: floor 18”x24” or wall 16”x24” and not under a door; below grade areaway 16”x24”.",
    "R408.5": "Removal of Debris: all organics and construction debris removed before occupancy",
    "R408.6": "Finished Grade: at least as high as the outside finished grade",
    "R408.7": "Flood: vent 1 square inch per square foot; grade at least as high as the outside finished grade",
}

R500_Floor_Framing = {
    "R317.2": "Joists 18 in, girders 12 in, posts or bearing on concrete 8 in",

    "R502.3": "Allowable joist spans, living areas: Table R502.3.1(2)\n\tAllowable joist spans, sleeping areas: Table R502.3.1(1)\n\tAllowable cantilever lengths: Table R502.3.3(1) or (2)",

    "R502.4": "Bearing walls on parallel joists: double joists, 2”x full depth blocked @ 4’ oc\n\tBearing walls perpendicular to joists, within the joist depth of the girder.",

    "R502.5": "Allowable Girder and Header Spans: see 602.7(1) (2) or (3) and excerpt below",

    "R502.6": "Bearing: min 1½” on wood; splices at bearing lap 3” with (3) 10d",

    "R502.7": "Joists must be laterally restrained (blocked) at all supports",

    "R502.8": "Cutting, Drilling, and Notching: See Fig R502.8\n\tDrilling: D/3, min 2” clear to edge\n\tNotching: D/3 x D/6 in end third; notches not allowed in middle third\n\tEnd Cut: D/4",

    "R502.9": "Fastening: See Table R602.3(1)",

    "R502.10": "Floor openings, use header and trimmer joists\n\tDouble header if > 4 ft;\n\tDouble trimmer if header is > 3 ft from trimmer bearing",

    "R502.11": "Wood Trusses: Engineering required; brace to prevent rotation; do not alter",

    "R502.13": "Fireblocking Required per R302.11. Most frequent locations include:\n\tConcealed stud walls: ceiling and floor levels, soffits, coves\n\tTop and bottom of stair stringers.\n\tAround openings at ceiling and floor levels (vents, pipes, wires, etc.)",

    "R502.12": "Draftstopping Required per R302.12",

    "R503.2": "Subfloor/Underlayment: min 19/32 or 5/8\n\tCheck label: to CSA O325, CSA O437 DOC PS 1 or DOC PS2",
    
    "R503.2": "Wood Structural Panel Sheathing:\n\tCombo Subfloor 16 o.c. 19/32 or 5/8\n\tCombo Subfloor 20 o.c. 19/32 or 5/8",
}

R506_SlabOnGrade = {
    "R402.2": "Concrete ACI 332 f′c = 2500 psi min (stem walls require 3,000 psi)",

    "R403.1.8": "Expansive soils, footing must be engineered or per CBO approval. Yolo Builds Policy: If no geotechnical report is provided, then assume the soil is expansive. CBO has preapproved slabs for conventional light-frame construction do not require engineered slabs if the slab is at least 5 inches thick with minimum reinforcement of #4 rebar in an 18” grid. Slabs with a live load of 40 psf or less may use #3 rebar in a 24” grid.",

    "R506.1": "General: min 3.5” thick; mix design must address bleeding, shrinkage, and curling.",

    "R506.2": "Site Preparation: remove all vegetation, topsoil, and foreign material.",

    "R506.2.1": "Fill must be compacted:\n\tMax fill, clean soil, 8 in\n\tMax fill, clean sand/gravel, 24 in.",
    
    "R506.2.2": "Base: min 4” thick; ½” or larger clean aggregate. Clean graded sand, gravel, crushed stone, crushed concrete or crushed blast-furnace slag passing a 2-inch (51 mm) sieve.",

    "R506.2.3": "Vapor Retarder: min 6-mil polyethylene lapped 6” directly contacting concrete.",

    "R506.2.4": "Reinforcement Support: must remain in center to upper one-third.",

    "CALGreen": "Conditioned Space: Capillary break, base is min ½ in clean aggregate; mix design to address bleeding, shrinkage and curling; Vapor retarder, min 10 mil ASTM E1745 class A, joints lapped min 6 in",
}

R507_Decks = {
    "R301.5": "Live Load for “Balconies (exterior) and decks” is 60 psf",

    "R507.2": "Materials: Grade #2 or better; preservative treated",

    "R507.3": "Footings: see Table 507.3.1 for min pier footing dimensions",

    "R507.4": "Deck Posts: 4”x4” to 6’-6”; 4”x6” to 8’; 6”x6” to 14’; use mechanical fastener or 12” embedment",

    "R507.5": "Deck Beams: Table 507.5; plies two rows of 10d @ 16” oc; cantilever max ¼ of span; 1½” bearing",

    "R507.6": "Deck Joists: Table 507.6; cantilever max ¼ of span; 1½” bearing; hardware on single ply beams; must be braced to prevent rotation.",

    "R507.7": "Decking: Table 507.7; min (2) 8d threaded nails or No 8 screws",

    "R507.8": "Vertical and Lateral Supports: positive connection; no toe nail or withdrawal",

    "R507.9": "Vertical and Lateral Supports at Band Joists",

    "R507.9.1.1": "Ledger: 2”x8” treated; no concentrated loads; not supported by veneer",

    "R507.9.1.2": "Band Joist: 2” nominal bearing fully on the primary structure capable of supporting loads",

    "R507.9.1.3": "Ledger to Band Joist: See Table 507.9.1.3(1)",

    "R507.9.2": "Lateral Connection; see details for 1500# and 750# devices",
}

R800_RoofCeiling = {
    "R801.3": "Expansive soils require a controlled method of water disposal from roofs to collect and discharge water not less than 5 feet from foundation walls.",

    "R802.2": "Provide continuous ties (ceiling joists) across the structure to prevent roof thrust applied to walls.", 

    "R802.3": "Ridge board min 1 inch wide by at least the depth of the cut end of the rater. If continuous ties are not provided, the rafters shall be supported by a wall or ridge beam supported on each end by a wall or column.",

    "R802.4": "Rafters shall be sized based on Table R802.4.1(1) – (8)",

    "R802.4.2": "Rafters shall be connected with a collar tie, ridge strap, or gusset plate.",

    "R802.4.3": "Hip and valley rafters min 2” by cut end of rafter, supported by a brace to bearing. ",

    "R802.4.4": "Roof pitch < 3:12, rafter support ridge, hip, and valley must be designed as beams.",

    "R802.6": "Rafters, ceiling joists shall bear at least 1.5” on wood or metal.",

    "R802.7": "Rafter notches per Fig R802.7.1.1",

    "R802.9": "Openings: Double if Header > 4 ft, Trimmer > 3 ft, or Tail > 12 ft. Use hangar if H > 6 ft",

    "R802.10": "Truss design drawings, prepared in conformance to R802.10, shall be provided to the building official and approved prior to installation.",

    "R802.11": "Required uplift resistance. Simpson H1 has allowable uplift of 480",

    "R803.2.1.1": "Exterior: wood sheathing permanently exposed to outdoor applications\n\tExposure I: exposed to the underside.",

    "R803.2.2": "Maximum allowable sheathing spans per Table R503.2.1.1(1):\n\tRoof 24/0, 3/8” with edge support\n\tRoof 24/16, 7/16” no edge support",
    
    "R806.2": "The minimum net free ventilating area shall be 1/150 of the area of the vented space. See exceptions, and approach to unvented attic space.",

    "R807.1": "Areas that have 30 in vertical height (top of joist to bottom of rafter) over an area of 30 sf or more shall have attic access.\n\tAccess shall have minimum head room of 30 in.\n\tOpening shall be min 22 x 30.",
}

structural = []
structural = [R301_Structural_Design_Criteria, R400_Foundations, R500_Floor_Framing, R506_SlabOnGrade, R507_Decks, R800_RoofCeiling]

if __name__ == "__main__":
    main(structural)
