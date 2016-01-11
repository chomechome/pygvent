# coding=utf-8
from pygvent.structures import Layer, Scene
from tests.mocks import MockGameObject, TestCaseWithPatch, \
    MockVisibleGameObject


class LayerTest(TestCaseWithPatch):
    def setUp(self):
        self.test_layer = Layer('TestLayer')
        self.test_objects = [MockGameObject() for _ in range(10)]
        self.test_object = self.test_objects[0]

    def test_add_object_to_layer(self):
        self.test_layer.add(self.test_object)
        self.assertIn(self.test_layer, self.test_object.layers)
        self.assertIn(self.test_object, self.test_layer)

    def test_add_layer_to_object(self):
        self.test_object.add_to_layer(self.test_layer)
        self.assertIn(self.test_layer, self.test_object.layers)
        self.assertIn(self.test_object, self.test_layer)

    def test_remove_object_from_layer(self):
        self.test_layer.add(self.test_object)
        self.test_layer.remove(self.test_object)

        self.assertNotIn(self.test_layer, self.test_object.layers)
        self.assertNotIn(self.test_object, self.test_layer)

    def test_remove_layer_from_object(self):
        self.test_object.add_to_layer(self.test_layer)
        self.test_object.remove_from_layer(self.test_layer)

        self.assertNotIn(self.test_layer, self.test_object.layers)
        self.assertNotIn(self.test_object, self.test_layer)

    def test_extend_layer(self):
        self.test_layer.extend(self.test_objects)

        self.assertEqual(len(self.test_objects), len(self.test_layer))

        for obj in self.test_objects:
            self.assertIn(self.test_layer, obj.layers)
            self.assertIn(obj, self.test_layer)

    def test_clear(self):
        self.test_layer.extend(self.test_objects)
        self.test_layer.clear()

        self.assertEqual(0, len(self.test_layer))

        for obj in self.test_objects:
            self.assertNotIn(self.test_layer, obj.layers)
            self.assertNotIn(obj, self.test_layer)

    def test_equality(self):
        self.test_layer.extend(self.test_objects)

        new_layer = Layer(self.test_layer.name)
        new_layer.extend(self.test_objects)
        self.assertEqual(self.test_layer, new_layer)

        new_layer.remove(self.test_object)
        self.assertNotEqual(self.test_layer, new_layer)

        self.assertNotEqual(self.test_layer, self.test_object)

    def test_copy(self):
        self.test_layer.extend(self.test_objects)

        new_layer = self.test_layer.copy()

        self.assertEqual(self.test_layer, new_layer)
        self.assertIsNot(self.test_layer, new_layer)

        for obj in new_layer:
            self.assertIn(self.test_layer, obj.layers)
            self.assertIn(new_layer, obj.layers)
            self.assertIn(obj, self.test_layer)

    def test_update(self):
        self.patch('tests.mocks.MockGameObject.update')

        self.test_layer.extend(self.test_objects)

        self.test_layer.update()

        self.assertEqual(len(self.test_objects),
                         MockGameObject.update.call_count)

    def test_draw(self):
        self.patch('tests.mocks.MockVisibleGameObject.draw')

        objects = [MockVisibleGameObject() for _ in range(13)]
        self.test_layer.extend(objects)

        test_screen = 'banana'
        self.test_layer.draw(test_screen)

        MockVisibleGameObject.draw.assert_called_with(test_screen)
        self.assertEqual(len(objects), MockVisibleGameObject.draw.call_count)


class SceneTest(TestCaseWithPatch):
    def setUp(self):
        self.test_scene = Scene()
        self.test_layers = [Layer('TestLayer{}'.format(i),
                                  [MockGameObject() for _ in range(i)])
                            for i in range(10)]
        self.test_layer = self.test_layers[-1]

    def test_add_layer(self):
        self.test_scene.add(self.test_layer)
        self.assertIn(self.test_layer, self.test_scene)

    def test_remove_layer(self):
        self.test_scene.add(self.test_layer)
        self.test_scene.remove(self.test_layer)
        self.assertNotIn(self.test_layer, self.test_scene)

    def test_remove_layer_by_name(self):
        self.test_scene.add(self.test_layer)
        self.test_scene.remove(self.test_layer.name)
        self.assertNotIn(self.test_layer, self.test_scene)

    def test_get_layer(self):
        self.test_scene.add(self.test_layer)

        name = self.test_layer.name
        self.assertIs(self.test_layer, self.test_scene[name])
        self.assertIs(self.test_layer, getattr(self.test_scene, name))

        self.assertRaises(AttributeError, getattr, self.test_scene,
                          'definitely not a layer in test scene')

    def test_extend(self):
        self.test_scene.extend(self.test_layers)

        self.assertEqual(len(self.test_layers), len(self.test_scene))
        for layer in self.test_layers:
            self.assertIn(layer, self.test_scene)
            self.assertIs(layer, self.test_scene[layer.name])
            self.assertIs(layer, getattr(self.test_scene, layer.name))

    def test_clear(self):
        test_layers_objects = [layer.objects for layer in self.test_layers]

        self.test_scene.extend(self.test_layers)
        self.test_scene.clear()

        self.assertEqual(0, len(self.test_scene))
        for layer, objects in zip(self.test_layers, test_layers_objects):
            self.assertNotIn(layer, self.test_scene)
            self.assertEqual(0, len(layer))
            for obj in objects:
                self.assertNotIn(obj, layer)
                self.assertNotIn(layer, obj.layers)

    def test_update(self):
        self.patch('pygvent.structures.Layer.update')

        self.test_scene.extend(self.test_layers)
        self.test_scene.update()

        self.assertEqual(len(self.test_layers), Layer.update.call_count)

    def test_draw(self):
        self.patch('pygvent.structures.Layer.draw')

        self.test_scene.extend(self.test_layers)

        test_screen = 'apple'
        self.test_scene.draw(test_screen)

        Layer.draw.assert_called_with(test_screen)
        self.assertEqual(len(self.test_layers), Layer.draw.call_count)
