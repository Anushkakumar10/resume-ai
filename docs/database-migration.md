# Database Migration Documentation

## Overview
This document provides detailed instructions for managing database migrations in the ResumeAI project. It covers setting up Flask-Migrate, performing schema updates, and migrating existing data without data loss.

---

### Table of Contents
1. [Introduction to Database Migrations](#introduction-to-database-migrations)
2. [Performing Schema Updates](#performing-schema-updates)
3. [Custom Migration Scripts for Existing Data](#custom-migration-scripts-for-existing-data)
4. [Best Practices](#best-practices)

---

## Introduction to Database Migrations
Database migrations allow developers to:
- Update the database schema incrementally.
- Track changes in the schema using version-controlled migration scripts.
- Safely alter the database structure without losing existing data.

**Tool Used:** Flask-Migrate, built on Alembic.

---

## Performing Schema Updates

### Steps to Update Schema
1. **Modify the Model:**
   Make changes to the database model in `app/models`.

2. **Generate a Migration Script:**
   Run the following command to create a migration script reflecting the changes:
   ```bash
   flask db migrate -m "Description of schema update"
   ```

3. **Apply the Migration:**
   Apply the changes to the database:
   ```bash
   flask db upgrade
   ```

### Example
- **Change:** Add a `profile_picture` column to the `User` table.
- **Command Output:**
  ```bash
  flask db migrate -m "Added profile_picture column to User table"
  ```

- Generated migration script (in `migrations/versions`):
    ```python
    def upgrade():
        op.add_column('users', sa.Column('profile_picture', sa.String(length=200), nullable=True))
    
    def downgrade():
        op.drop_column('users', 'profile_picture')
    ```

---

## Custom Migration Scripts for Existing Data

### Objective
If schema updates require transforming or populating data, custom migration scripts can be used.

### Example Script
Suppose we add a `skills` JSON column to the `User` table. We need to populate it with default values for existing users.

1. **Generate Migration Script:**
   ```bash
   flask db migrate -m "Add skills column to User table"
   ```

2. **Modify Migration Script:**
   Edit the script in the `migrations/versions` folder:
   ```python
   def upgrade():
       op.add_column('users', sa.Column('skills', sa.JSON, nullable=True))

       # Populate existing users with default skills
       from sqlalchemy.sql import table, column
       from sqlalchemy.dialects import postgresql

       users_table = table(
           'users',
           column('id', sa.Integer),
           column('skills', postgresql.JSON)
       )

       default_skills = [{"name": "Unspecified", "level": "beginner"}]
       op.execute(users_table.update().values(skills=default_skills))

   def downgrade():
       op.drop_column('users', 'skills')
   ```

3. **Apply the Migration:**
   ```bash
   flask db upgrade
   ```

---

## Best Practices

1. **Backup the Database:**
   Always back up the database before running migrations in production.

2. **Review Generated Scripts:**
   Flask-Migrate generates scripts automatically, but you should always review and test them.

3. **Version Control:**
   Commit migration scripts to your version control system (e.g., Git).

4. **Test Migrations:**
   Test migrations in a staging environment before applying them to production.

5. **Document Changes:**
   Document schema updates and the purpose of each migration for future reference.

---

### Troubleshooting

#### Common Issues
- **Migration script errors:**
  Ensure models and migrations are in sync. Delete the migration script, fix the model, and re-run `flask db migrate`.

- **`Target database is not up to date`:**
  Run `flask db upgrade` to bring the database to the latest version.

---

This document ensures you can manage database migrations efficiently and maintain data integrity throughout the project's lifecycle.