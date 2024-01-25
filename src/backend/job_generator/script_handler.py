def start_script() -> str:
    return "pipeline{\n\tagent any\n\tstages{"


def end_script() -> str:
    return "\n\t}\n}"


def start_stage(stage_name: str) -> str:
    return (f"\n\t\tstage('{stage_name}')" + "{\n\t\t\tsteps{\n\t\t\t\t"
            + f"echo '##################### {stage_name} Stage #####################'")


def end_stage() -> str:
    return "\n\t\t\t}\n\t\t}"


def write_step(step_command: str) -> str:
    return f"\n\t\t\t\t{step_command}"
