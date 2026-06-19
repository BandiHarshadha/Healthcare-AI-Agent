# Rollback Procedure

If Healthcare AI Agent gives unsafe output or production fails:

1. Stop backend server.
2. Revert to previous Git commit.
3. Restart FastAPI backend.
4. Test /api/health/check endpoint.
5. Inform team lead.