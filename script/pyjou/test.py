from pyjou import Journal

jou = Journal()
jou.file.read_case.set('cas/case.cas')
jou.file.read_journal.set('jou-1.jou', 'jou-2.jou')
jou.file.mesh_replace.set('msh/mesh.msh')
jou.file.write_case.set('cas/new.cas')
jou.file.write_case_data.set('cas/new-cas-dat.cas')
jou.define.boundary_conditions.velocity_inlet.set('inlet', 10, 300)
jou.define.boundary_conditions.pressure_outlet.set('outlet', 300)
jou.define.boundary_conditions.wall.set('wall-1', 1000)
jou.define.models.viscous.set('kw-sst')
jou.define.models.viscous.near_wall_treatment.set('enhanced-wall-treatment')
jou.surface.line_surface.set('line-1', 0, 0, 0, .005)
jou.surface.point_surface.set('pt-1', 0, 2)
jou.mesh.translate.set(10, 0)
jou.mesh.modify_zones.append_mesh.set('msh/new-msh.msh')
jou.mesh.modify_zones.merge_zones.set('one-zone', 'another-zone')
jou.mesh.modify_zones.fuse_face_zones.set('one-zone', 'another-zone')
jou.mesh.modify_zones.zone_name.set('old', 'new')
jou.mesh.check.set()
jou.mesh.repair_improve.repair.set()
jou.solve.monitors.residual.convergence_criteria.set(1e-6)
jou.solve.initialize.initialize_flow.set()
jou.solve.initialize.compute_defaults.velocity_inlet.set('zone')
jou.solve.iterate.set(1e3)
jou.report.fluxes.mass_flow.set('out/out.txt', 'one-zone', 'another-zone')
jou.report.fluxes.heat_transfer.set('out/out.txt', all_zones = True)
jou.report.surface_integrals.area.set('out/out.txt', 'one-zone', 'another-zone')
jou.report.surface_integrals.facet_avg.set('out/out.txt', 'velocity', 'axis')
jou.save('worked.jou')