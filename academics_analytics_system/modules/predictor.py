from modules.intelligence.history import (
    get_student_record_from_dataset,
    get_student_academic_history
)

from modules.intelligence.performance import (
    build_student_performance_series,
    build_performance_series_entry
)

from modules.intelligence.trends import (
    analyze_student_trend,
    extract_metric_changes,
    build_trend_steps
)

from modules.intelligence.risk import (
    get_latest_performance_entry,
    analyze_student_risk
)

from modules.intelligence.prediction import (
    predict_student_performance
)

from modules.intelligence.advanced_analysis import (
    compare_internal_board_performance,
    analyze_weakness_persistence,
    analyze_academic_stability,
    analyze_improvement_momentum,
    analyze_subject_comovement,
    analyze_exam_context,
    analyze_cohort_performance,
    analyze_subject_consistency
) 