import graphene


class CreateProject(graphene.Mutation):
    id = graphene.ID()
    class Arguments:
        name = graphene.String(required=True)
    def mutate(self, info, **args):
        return CreateProject(id=1)


class CreateProject2(CreateProject):
    def mutate(self, info, **args):
        args['foo'] = 1
        return super().mutate(info, **args)


class Mutation(graphene.ObjectType):
    create_project = CreateProject2.Field()


schema = graphene.Schema(mutation=Mutation)
