import streamlit as st
from services.config.workout_config import METRICS_FIELDS


def async_metrics_update(context):
    """
    Asynchronous function to update metrics.
    This function is intended to be called periodically to refresh the metrics data.
    """
    # Implementation for updating metrics goes here
    if not context or not hasattr(context, 'state') or not context.state.playing:
        return

    processor = getattr(context, 'video_processor', None)

    exercise = st.session_state.get("exercise_type")

    if not exercise:
        return

    processor.set_exercise(exercise)
    latest_metrics = processor.get_latest_metrics()

    if not latest_metrics:
        return

    # Update the metrics in the session state
    reps = latest_metrics.get("reps", 0)
    st.session_state["reps"] = reps


    fields = METRICS_FIELDS.get(exercise, [])
    for field in fields:
        if field in latest_metrics:
            st.session_state[field] = latest_metrics[field]

    reps_per_set = st.session_state.get("reps_per_set", 0)
    target_sets = st.session_state.get("target_sets", 0)

    if reps_per_set > 0 and target_sets > 0:
        sets_completed = reps // reps_per_set
        current_set_reps = reps % reps_per_set
        workout_completed = sets_completed >= target_sets
        
    else:
        sets_completed = 0
        current_set_reps = 0
        workout_completed = False

    st.session_state.sets_completed = sets_completed
    st.session_state.current_set_reps = current_set_reps
    st.session_state.workout_completed = workout_completed
