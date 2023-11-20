from main import HD, act_eval, evaluate, evaluate_lazy


def test_equal_true():
    expr = "(namespace.a == 1)"
    namespace = {"namespace": [HD({"a": 1, "b": 2}), HD({"a": 2, "b": 2})]}
    result = {"namespace": [HD({"a": 1, "b": 2})]}
    result_bool = True

    evaluated = evaluate(act_eval(expr, namespace))
    assert evaluated == result

    evaluated = evaluate_lazy(act_eval(expr, namespace))
    assert evaluated == result_bool


def test_equal_false():
    expr = "(namespace.a == 3)"
    namespace = {"namespace": [HD({"a": 1, "b": 2}), HD({"a": 2, "b": 2})]}
    result = {"namespace": []}
    result_bool = False

    evaluated = evaluate(act_eval(expr, namespace))
    assert evaluated == result

    evaluated = evaluate_lazy(act_eval(expr, namespace))
    assert evaluated == result_bool


def test_and_true():
    expr = "namespace.b == 2 and namespace.a == 1"
    namespace = {"namespace": [HD({"a": 1, "b": 2}), HD({"a": 2, "b": 2})]}
    result = {"namespace": [HD({"a": 1, "b": 2})]}
    result_bool = True

    evaluated = evaluate(act_eval(expr, namespace))
    assert evaluated == result

    evaluated = evaluate_lazy(act_eval(expr, namespace))
    assert evaluated == result_bool


def test_and_false():
    expr = "namespace.b == -1 and namespace.a == 1"
    namespace = {"namespace": [HD({"a": 1, "b": 2}), HD({"a": 2, "b": 2})]}
    result = {"namespace": []}
    result_bool = False

    evaluated = evaluate(act_eval(expr, namespace))
    assert evaluated == result

    evaluated = evaluate_lazy(act_eval(expr, namespace))
    assert evaluated == result_bool


def test_or_true():
    expr = "namespace.b == 2 or namespace.a == 1"
    namespace = {"namespace": [HD({"a": 1, "b": 2}), HD({"a": 2, "b": 2})]}
    result = {"namespace": [HD({"a": 1, "b": 2}), HD({"a": 2, "b": 2})]}
    result_bool = True

    evaluated = evaluate(act_eval(expr, namespace))
    assert evaluated == result

    evaluated = evaluate_lazy(act_eval(expr, namespace))
    assert evaluated == result_bool

def test_or_false():
    expr = "namespace.b == 20 or namespace.a == 11"
    namespace = {"namespace": [HD({"a": 1, "b": 2}), HD({"a": 2, "b": 2})]}
    result = {"namespace": []}
    result_bool = False

    evaluated = evaluate(act_eval(expr, namespace))
    assert evaluated == result

    evaluated = evaluate_lazy(act_eval(expr, namespace))
    assert evaluated == result_bool

def test_gt_true():
    expr = "namespace.a > 1"
    namespace = {"namespace": [HD({"a": 1, "b": 2}), HD({"a": 2, "b": 2})]}
    result = {"namespace": [HD({"a": 2, "b": 2})]}
    result_bool = True

    evaluated = evaluate(act_eval(expr, namespace))
    assert evaluated == result

    evaluated = evaluate_lazy(act_eval(expr, namespace))
    assert evaluated == result_bool

def test_gt_false():
    expr = "namespace.a > 10"
    namespace = {"namespace": [HD({"a": 1, "b": 2}), HD({"a": 2, "b": 2})]}
    result = {"namespace": []}
    result_bool = False

    evaluated = evaluate(act_eval(expr, namespace))
    assert evaluated == result

    evaluated = evaluate_lazy(act_eval(expr, namespace))
    assert evaluated == result_bool

def test_gte():
    expr = "namespace.a >= 1"
    namespace = {
        "namespace": [HD({"a": 1, "b": 2}), HD({"a": 2, "b": 2})],
    }
    result = {"namespace": [HD({"a": 1, "b": 2}), HD({"a": 2, "b": 2})]}

    evaluated = evaluate(act_eval(expr, namespace))
    assert evaluated == result


def test_cast_int():
    expr = "int(namespace.a) == 1"
    namespace = {
        "namespace": [HD({"a": "1", "b": "2"}), HD({"a": "2", "b": "2"})],
    }
    result = {"namespace": [HD({"a": "1", "b": "2"})]}

    evaluated = evaluate(act_eval(expr, namespace))
    assert evaluated == result


def test_cast_float():
    expr = "float(namespace.a) == 1"
    namespace = {
        "namespace": [HD({"a": "1", "b": "2"}), HD({"a": "2", "b": "2"})],
    }
    result = {"namespace": [HD({"a": "1", "b": "2"})]}

    evaluated = evaluate(act_eval(expr, namespace))
    assert evaluated == result


def test_in():
    expr = "namespace.a in ['1', '2']"
    namespace = {"namespace": [HD(a="1"), HD(a="2"), HD(a="3")]}
    result = {"namespace": [HD(a="1"), HD(a="2")]}

    evaluated = evaluate(act_eval(expr, namespace))
    assert evaluated == result
