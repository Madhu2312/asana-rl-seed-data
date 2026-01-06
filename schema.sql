PRAGMA foreign_keys = ON;

-- ===============================
-- ORGANIZATION & PEOPLE
-- ===============================

CREATE TABLE organizations (
    org_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL
);

CREATE TABLE teams (
    team_id TEXT PRIMARY KEY,
    org_id TEXT NOT NULL,
    name TEXT NOT NULL,
    FOREIGN KEY (org_id) REFERENCES organizations(org_id)
);

CREATE TABLE users (
    user_id TEXT PRIMARY KEY,
    org_id TEXT NOT NULL,
    full_name TEXT NOT NULL,
    email TEXT NOT NULL,
    role TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    FOREIGN KEY (org_id) REFERENCES organizations(org_id)
);

CREATE TABLE team_memberships (
    team_id TEXT NOT NULL,
    user_id TEXT NOT NULL,
    PRIMARY KEY (team_id, user_id),
    FOREIGN KEY (team_id) REFERENCES teams(team_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- ===============================
-- PROJECT STRUCTURE
-- ===============================

CREATE TABLE projects (
    project_id TEXT PRIMARY KEY,
    team_id TEXT NOT NULL,
    name TEXT NOT NULL,
    project_type TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    FOREIGN KEY (team_id) REFERENCES teams(team_id)
);

CREATE TABLE sections (
    section_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    name TEXT NOT NULL,
    position INTEGER NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- ===============================
-- TASKS & SUBTASKS
-- ===============================

CREATE TABLE tasks (
    task_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    section_id TEXT NOT NULL,
    assignee_id TEXT,
    name TEXT NOT NULL,
    description TEXT,
    due_date DATE,
    completed BOOLEAN NOT NULL,
    created_at TIMESTAMP NOT NULL,
    completed_at TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id),
    FOREIGN KEY (section_id) REFERENCES sections(section_id),
    FOREIGN KEY (assignee_id) REFERENCES users(user_id)
);

CREATE TABLE subtasks (
    subtask_id TEXT PRIMARY KEY,
    parent_task_id TEXT NOT NULL,
    assignee_id TEXT,
    name TEXT NOT NULL,
    completed BOOLEAN NOT NULL,
    created_at TIMESTAMP NOT NULL,
    completed_at TIMESTAMP,
    FOREIGN KEY (parent_task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (assignee_id) REFERENCES users(user_id)
);

-- ===============================
-- COMMENTS
-- ===============================

CREATE TABLE comments (
    comment_id TEXT PRIMARY KEY,
    task_id TEXT NOT NULL,
    user_id TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    FOREIGN KEY (task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- ===============================
-- CUSTOM FIELDS
-- ===============================

CREATE TABLE custom_field_definitions (
    field_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    name TEXT NOT NULL,
    field_type TEXT NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

CREATE TABLE custom_field_values (
    task_id TEXT NOT NULL,
    field_id TEXT NOT NULL,
    value TEXT NOT NULL,
    PRIMARY KEY (task_id, field_id),
    FOREIGN KEY (task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (field_id) REFERENCES custom_field_definitions(field_id)
);

-- ===============================
-- TAGS
-- ===============================

CREATE TABLE tags (
    tag_id TEXT PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE task_tags (
    task_id TEXT NOT NULL,
    tag_id TEXT NOT NULL,
    PRIMARY KEY (task_id, tag_id),
    FOREIGN KEY (task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id)
);
