from model.project import Project
import random


def test_delete_some_group(app):
    if len(app.get_project_list()) == 0:
        app.project.create(Project(name="test"))
    old_projects = app.get_project_list()
    project = random.choice(old_projects)
    app.group.delete_project_by_id(project.id)
    assert len(old_projects) - 1 == app.project.count()
    new_projects = app.get_project_list()
    old_projects.remove(project)
    assert old_projects == new_projects
    assert sorted(new_projects, key=Project.id_or_max) == sorted(app.project.get_project_list(), key=Project.id_or_max)