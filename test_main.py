from main import HD, prepare_eval_parse, evaluate, evaluate_lazy


def test_equal_true():
    expr = "(namespace.a == 1)"
    namespace = {"namespace": [HD({"a": 1, "b": 2}), HD({"a": 2, "b": 2})]}
    result = {"namespace": [HD({"a": 1, "b": 2})]}
    result_bool = True

    evaluated = evaluate(prepare_eval_parse(expr, namespace))
    assert evaluated == result

    evaluated = evaluate_lazy(prepare_eval_parse(expr, namespace))
    assert evaluated == result_bool


def test_equal_false():
    expr = "(namespace.a == 3)"
    namespace = {"namespace": [HD({"a": 1, "b": 2}), HD({"a": 2, "b": 2})]}
    result = {"namespace": []}
    result_bool = False

    evaluated = evaluate(prepare_eval_parse(expr, namespace))
    assert evaluated == result

    evaluated = evaluate_lazy(prepare_eval_parse(expr, namespace))
    assert evaluated == result_bool


def test_and_true():
    expr = "namespace.b == 2 and namespace.a == 1"
    namespace = {"namespace": [HD({"a": 1, "b": 2}), HD({"a": 2, "b": 2})]}
    result = {"namespace": [HD({"a": 1, "b": 2})]}
    result_bool = True

    evaluated = evaluate(prepare_eval_parse(expr, namespace))
    assert evaluated == result

    evaluated = evaluate_lazy(prepare_eval_parse(expr, namespace))
    assert evaluated == result_bool


def test_and_false():
    expr = "namespace.b == -1 and namespace.a == 1"
    namespace = {"namespace": [HD({"a": 1, "b": 2}), HD({"a": 2, "b": 2})]}
    result = {"namespace": []}
    result_bool = False

    evaluated = evaluate(prepare_eval_parse(expr, namespace))
    assert evaluated == result

    evaluated = evaluate_lazy(prepare_eval_parse(expr, namespace))
    assert evaluated == result_bool


def test_or_true():
    expr = "namespace.b == 2 or namespace.a == 1"
    namespace = {"namespace": [HD({"a": 1, "b": 2}), HD({"a": 2, "b": 2})]}
    result = {"namespace": [HD({"a": 1, "b": 2}), HD({"a": 2, "b": 2})]}
    result_bool = True

    evaluated = evaluate(prepare_eval_parse(expr, namespace))
    assert evaluated == result

    evaluated = evaluate_lazy(prepare_eval_parse(expr, namespace))
    assert evaluated == result_bool

def test_or_true_regression():
    expr = "namespace.a == 1 and (namespace.b == -2 or namespace.a == 1)"
    namespace = {"namespace": [HD({"a": 1, "b": 2}), HD({"a": 2, "b": 2})]}
    result = {"namespace": [HD({"a": 1, "b": 2})]}
    result_bool = True

    evaluated = evaluate(prepare_eval_parse(expr, namespace))
    assert evaluated == result

    evaluated = evaluate_lazy(prepare_eval_parse(expr, namespace))
    assert evaluated == result_bool


def test_or_false():
    expr = "namespace.b == 20 or namespace.a == 11"
    namespace = {"namespace": [HD({"a": 1, "b": 2}), HD({"a": 2, "b": 2})]}
    result = {"namespace": []}
    result_bool = False

    evaluated = evaluate(prepare_eval_parse(expr, namespace))
    assert evaluated == result

    evaluated = evaluate_lazy(prepare_eval_parse(expr, namespace))
    assert evaluated == result_bool


def test_gt_true():
    expr = "namespace.a > 1"
    namespace = {"namespace": [HD({"a": 1, "b": 2}), HD({"a": 2, "b": 2})]}
    result = {"namespace": [HD({"a": 2, "b": 2})]}
    result_bool = True

    evaluated = evaluate(prepare_eval_parse(expr, namespace))
    assert evaluated == result

    evaluated = evaluate_lazy(prepare_eval_parse(expr, namespace))
    assert evaluated == result_bool


def test_gt_false():
    expr = "namespace.a > 10"
    namespace = {"namespace": [HD({"a": 1, "b": 2}), HD({"a": 2, "b": 2})]}
    result = {"namespace": []}
    result_bool = False

    evaluated = evaluate(prepare_eval_parse(expr, namespace))
    assert evaluated == result

    evaluated = evaluate_lazy(prepare_eval_parse(expr, namespace))
    assert evaluated == result_bool


def test_gte():
    expr = "namespace.a >= 1"
    namespace = {
        "namespace": [HD({"a": 1, "b": 2}), HD({"a": 2, "b": 2})],
    }
    result = {"namespace": [HD({"a": 1, "b": 2}), HD({"a": 2, "b": 2})]}

    evaluated = evaluate(prepare_eval_parse(expr, namespace))
    assert evaluated == result


def test_cast_int():
    expr = "int(namespace.a) == 1"
    namespace = {
        "namespace": [HD({"a": "1", "b": "2"}), HD({"a": "2", "b": "2"})],
    }
    result = {"namespace": [HD({"a": "1", "b": "2"})]}

    evaluated = evaluate(prepare_eval_parse(expr, namespace))
    assert evaluated == result


def test_cast_float():
    expr = "float(namespace.a) == 1"
    namespace = {
        "namespace": [HD({"a": "1", "b": "2"}), HD({"a": "2", "b": "2"})],
    }
    result = {"namespace": [HD({"a": "1", "b": "2"})]}

    evaluated = evaluate(prepare_eval_parse(expr, namespace))
    assert evaluated == result


def test_in():
    expr = "namespace.a in ['1', '2']"
    namespace = {"namespace": [HD(a="1"), HD(a="2"), HD(a="3")]}
    result = {"namespace": [HD(a="1"), HD(a="2")]}

    evaluated = evaluate(prepare_eval_parse(expr, namespace))
    assert evaluated == result


def test_in_tuple():
    expr = "namespace.a in ('1', '2')"
    namespace = {"namespace": [HD(a="1"), HD(a="2"), HD(a="3")]}
    result = {"namespace": [HD(a="1"), HD(a="2")]}

    evaluated = evaluate(prepare_eval_parse(expr, namespace))
    assert evaluated == result

def test_neq_true():
    expr = "namespace.a != '1'"
    namespace = {"namespace": [HD(a="1"), HD(a="2"), HD(a="3")]}
    result = {"namespace": [HD(a="2"), HD(a="3")]}

    evaluated = evaluate(prepare_eval_parse(expr, namespace))
    assert evaluated == result

def test_neq_false():
    expr = "namespace.a != '1' and namespace.a != '2' and namespace.a != '3'"
    namespace = {"namespace": [HD(a="1"), HD(a="2")]}
    result = {"namespace": []}

    evaluated = evaluate(prepare_eval_parse(expr, namespace))
    assert evaluated == result

def test_multiple_or():
    expr = "namespace.a == '1' or namespace.a == '2' or namespace.a == '3'"
    namespace = {"namespace": [HD(a="1"), HD(a="2"), HD(a="3")]}
    result = {"namespace": [HD(a="1"), HD(a="2"), HD(a="3")]}

    evaluated = evaluate(prepare_eval_parse(expr, namespace))
    assert evaluated == result
