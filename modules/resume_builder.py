def build_tailored_resume(resume_text, match_result):
    matched=match_result.get("matched_keywords",[])
    missing=match_result.get("missing_keywords",[])
    score=match_result.get("match_percentage",0.0)
    matched_str=", ".join(matched)if matched else "None"
    missing_str=", ".join(missing)if missing else "None"
    recommended_block=(f"Suggested Additional Skills:\n{missing_str}\n"
        if missing
        else "Your resume already matches all major job requirements!\n"
    )
    final_output = f"""
===============================
 AI Resume Tailoring Result
===============================

Match Score: {score}%


Matched Skills:
{matched_str}


Missing Skills (Recommended to Add):
{missing_str}


{recommended_block}

------------ Tailored Resume ------------
{resume_text}

------------ Suggestions ----------------
Include the missing skills in:
- Skills section
- Experience section
- Projects section

This will significantly improve your ATS score.
"""

    return final_output


 